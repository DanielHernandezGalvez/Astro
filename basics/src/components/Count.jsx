
import React, { useState } from "react";

const Count = () => {
  const [count, setCount] = useState(0);

  const handleClick = () => {
    setCount(count + 1);
    console.log(count)
  };

  return (
    <div>
      <button className="bg-gray-500 text-white p-3" onClick={handleClick}>Click me!</button>
      <p>The count is: {count}</p>
    </div>
  );
};

export default Count;