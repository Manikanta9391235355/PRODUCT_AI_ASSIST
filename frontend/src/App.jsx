import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);
  const [query, setQuery] = useState("");
  const [summary, setSummary] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products")
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  const handleAsk = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await res.json();
    setProducts(data.products);
    setSummary(data.summary);
  };

  return (
    <div>
      <h1>Product AI Assist</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleAsk}>Ask</button>

      <p>{summary}</p>

      {products.map(p => (
        <div key={p.id}>
          <h3>{p.name}</h3>
          <p>{p.description}</p>
          <p>${p.price}</p>
        </div>
      ))}
    </div>
  );
}

export default App;