import { useState } from 'react';

function App() {
  const [data, setData] = useState({});

  const fetchData = async (dynamicString) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/${dynamicString}`);
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className='App'>
      <h1>Animals Facts</h1>
      <button onClick={() => fetchData('animal/lion')}>Lion 🦁</button>
      <button onClick={() => fetchData('animal/elephant')}>Elephant 🐘</button>
      <button onClick={() => fetchData('animal/giraffe')}>Giraffe 🦒</button>
      <h3> {data.name} </h3>
      <h6> {data.description} </h6>
    </div>
  );
}

export default App;
