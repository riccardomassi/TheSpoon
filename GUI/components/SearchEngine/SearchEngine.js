'use client';
import { useState } from 'react';
import Searchbar from '../SearchBar/Searchbar';
import Results from '../Results/Results';

const SearchEngine = () => {
	const [results, setResults] = useState([]);

	const handleSearchResults = (apiResults) => {
		setResults(apiResults);
	};

	return (
		<div className="flex flex-col w-screen h-screen items-center justify-center">
			<Searchbar onSearchResults={handleSearchResults} />
			<Results results={results} />
		</div>
	);
};

export default SearchEngine;
