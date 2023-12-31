import React from 'react';

const SkillCard = ({ label }) => {
  return (
    <div
      class="border rounded-full  opacity-80 hover:bg-blue-500 
      cursor-pointer hover:text-white transition hover:scale-105
      py-1 px-2 lg:py-2 lg:px-4 text-xs lg:text-base"
    >
      {label}
    </div>
  );
};

export default SkillCard;