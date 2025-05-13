import { useState } from 'react';
import './App.css';

function App() {
  const [dataType, setDataType] = useState('text');
  const [minCount, setMinCount] = useState(10);
  const [maxCount, setMaxCount] = useState(100);
  const [response, setResponse] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch('http://127.0.0.1:8000/generator/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        data_type: dataType,
        min_count: minCount,
        max_count: maxCount
      })
    });

    const data = await res.json();
    setResponse(data);
  };

  return (
    <div className="container">
      <h1>FastIQ: Synthetic Data Generator</h1>
      <form onSubmit={handleSubmit}>
        <label>Data Type:</label>
        <input value={dataType} onChange={(e) => setDataType(e.target.value)} />

        <label>Min Count:</label>
        <input
          type="number"
          value={minCount}
          onChange={(e) => setMinCount(Number(e.target.value))}
        />

        <label>Max Count:</label>
        <input
          type="number"
          value={maxCount}
          onChange={(e) => setMaxCount(Number(e.target.value))}
        />

        <button type="submit">Generate</button>
      </form>

      {response && (
        <div className="response">
          <h2>Response</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
