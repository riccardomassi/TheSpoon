import React from 'react';
import Searchbar from '@/components/SearchBar/Searchbar';
import Results from '@/components/Results/Results';

const SearchEnginePage = () => {
	return (
		<div className="flex flex-col w-screen h-screen bg-slate-100 dark:bg-slate-800 flex-auto items-center justify-center">
			<Searchbar />
			<Results />
		</div>
	);
};

export default SearchEnginePage;
