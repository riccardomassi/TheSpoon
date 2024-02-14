'use client';
import { useState } from 'react';
import Searchbar from '../SearchBar/Searchbar';
import Results from '../Results/Results';

const SearchEngine = () => {
	const [results, setResults] = useState([]);
	const [error, setError] = useState(false);

	const handleSearchResults = (apiResults) => {
		setResults(apiResults);
	};

	const handleSearchError = (apiResults) => {
		setError(apiResults);
	};

	return (
		<div className="flex flex-col w-screen h-screen items-center justify-center">
			<Searchbar
				onSearchResults={handleSearchResults}
				onSearchError={handleSearchError}
			/>
			<Results results={results} error={error} />
		</div>
	);
};

export default SearchEngine;
