import React from 'react';

const SkillCard = ({ label }) => {
  return (
    <div
      class="border rounded-full px-5 opacity-80 hover:bg-blue-500 cursor-pointer hover:text-white transition hover:scale-105"
    >
      {label}
    </div>
  );
};

export default SkillCard;