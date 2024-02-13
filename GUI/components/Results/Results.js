import React from 'react';

const Results = ({ results }) => {
	console.log(results);
	return (
		<div className="text-4xl w-[90vw] h-[75vh] absolute top-56 bg-gray-200 dark:bg-gray-700 rounded">
			<div>{results}</div>
		</div>
	);
};

export default Results;
