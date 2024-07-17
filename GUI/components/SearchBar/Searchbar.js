'use client';
import { React, useState } from 'react';
import { Search } from 'lucide-react';
import { Checkbox } from '../ui/checkbox';
import { Rating, CircularProgress } from '@mui/material';

const Searchbar = ({ onSearchResults, onSearchError }) => {
	const [rating, setRating] = useState(1);
	const [checked, setChecked] = useState(false);
	const [sentiment, setSentiment] = useState('');
	const [searchValue, setSearchValue] = useState('');
	const [sorting, setSorting] = useState('');
	const [loading, setLoading] = useState(false);
	const [suggestions, setSuggestions] = useState([]);

	const handleAutoexp = (event) => {
		setChecked(event);
	};

	const handleSorting = (event) => {
		setSorting(event.target.value);
	};

	const handleSearchValue = (event) => {
		setSearchValue(event.target.value);
	};

	const handleSentiment = (event) => {
		setSentiment(event.target.value);
	};

	const apiRequest = async (query) => {
		setLoading(true);
		try {
			// Prepare the data to be sent in the request body
			const requestData = {
				searchValue: query || searchValue,
				rating,
				checked,
				sentiment,
				sorting,
			};

			// Effettua la chiamata API per eseguire la query e avere la risposta
			const response = await fetch('http://localhost:5050/api/search', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(requestData),
			});

			const apiResults = await response.json();
			if (apiResults.results.length === 0) {
				onSearchError(true);
				setSuggestions(apiResults.new_phrase.split(' '));
			} else {
				onSearchError(false);
				setSuggestions([]);
			}
			onSearchResults(apiResults.results);
			setSearchValue(query || searchValue);
		} catch (error) {
			console.error('Errore durante la chiamata API:', error);
		} finally {
			setLoading(false);
		}
	};

	const handleSuggestionClick = (suggestion) => {
		setSearchValue(suggestion);
		apiRequest(suggestion);
	};

	return (
		<div className="w-full absolute top-20 flex flex-col">
			<div className="flex flex-row justify-between">
				<div className="w-full mx-10">
					<label className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">
						Search
					</label>
					<div className="relative">
						<div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
							<Search />
						</div>
						<input
							className="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
							type="search"
							id="default-search"
							placeholder="Search..."
							required
							value={searchValue}
							onChange={handleSearchValue}
						/>
						<button
							className="text-white absolute end-2.5 bottom-2.5 bg-blue-600 hover:bg-blue-700 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 flex items-center justify-center"
							onClick={() => apiRequest()}
							disabled={loading}
						>
							{loading ? <CircularProgress size={24} color="inherit" /> : 'Search'}
						</button>
					</div>
					{suggestions.length > 0 && (
						<div className='flex flex-row items-center mt-2'>
							<p>forse stavi cercando: </p>
							<>
								{suggestions.map((suggestion, index) => (
									<span
										key={index}
										className="text-blue-600 hover:text-blue-800 cursor-pointer mx-1"
										onClick={() => handleSuggestionClick(suggestion)}
									>
										{suggestion}
									</span>
								))}
							</>
						</div>
					)}
				</div>
				<div className="w-1/2 mx-10">
					<div className="relative">
						<input
							className="block w-full p-4 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
							type="search"
							id="default-search"
							placeholder="Sentiment search (joy, anger, ...)"
							value={sentiment}
							onChange={handleSentiment}
						/>
					</div>
				</div>
			</div>
			<div className="flex flex-row w-full justify-center mt-6">
				<div className="mx-48">
					<select
						value={sorting}
						onChange={handleSorting}
						className="rounded p-2 bg-slate-300 dark:bg-slate-600 hover:bg-slate-200 hover:dark:bg-slate-500 text-black dark:text-white"
					>
						<option value={''}>Default</option>
						<option value={'reviewTime'}>Review Date</option>
						<option value={'reviewStars'}>Review Stars</option>
					</select>
				</div>
				<div className="flex flex-col items-center mx-48">
					<label>Ratings</label>
					<Rating
						name="simple-controlled"
						value={rating}
						onChange={(event, newRating) => {
							// Ensure the minimum rating is 1
							const clampedRating = Math.max(1, newRating);
							setRating(clampedRating);
						}}
					/>
				</div>
				<div className="flex items-center space-x-2 mx-48">
					<Checkbox
						id="autoexp"
						checked={checked}
						onCheckedChange={handleAutoexp}
					/>
					<label>Auto Expansion</label>
				</div>
			</div>
		</div>
	);
};

export default Searchbar;
