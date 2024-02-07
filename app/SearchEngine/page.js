import React from 'react';
import Searchbar from '@/components/SearchBar/Searchbar';

const SearchEnginePage = () => {
	return (
		<div className="flex flex-col w-screen h-screen bg-slate-100 dark:bg-slate-800 flex-auto items-center justify-center">
			<Searchbar />
			<div className="w-[85vw] h-[75vh] mt-48 bg-gray-200 dark:bg-gray-700 rounded"></div>
		</div>
	);
};

export default SearchEnginePage;
