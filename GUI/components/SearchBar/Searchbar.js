'use client';
import { React, useState } from 'react';
import { Search } from 'lucide-react';
import { Checkbox } from '../ui/checkbox';
import { Rating } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';

const Searchbar = () => {
	const [rating, setRating] = useState(1);
	const [checked, setChecked] = useState(false);
	const [sentiment, setSentiment] = useState('Positive');

	const handleAutoexp = (event) => {
		setChecked(event);
	};

	const handleSentiment = (event) => {
		setSentiment(event.target.value);
	};

	return (
		<form className="w-1/2 absolute top-16 flex flex-col">
			<div>
				<label className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">
					Search
				</label>
				<div className="relative">
					<div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
						<Search />
					</div>
					<input
						className="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white "
						type="search"
						id="default-search"
						placeholder="Search..."
						required
					/>
					<button
						type="submit"
						className="text-white absolute end-2.5 bottom-2.5 bg-blue-600 hover:bg-blue-700 focus:outline-non font-medium rounded-lg text-sm px-4 py-2"
					>
						Search
					</button>
				</div>
			</div>
			<div className="flex flex-row justify-between mt-6">
				<div>
					<Select
						labelId="demo-simple-select-label"
						id="demo-simple-select"
						value={sentiment}
						label="Age"
						onChange={handleSentiment}
						className="text-black dark:text-white border border-white"
					>
						<MenuItem value={'VeryPositive'}>Very Positive</MenuItem>
						<MenuItem value={'Positive'}>Positive</MenuItem>
						<MenuItem value={'Neutral'}>Neutral</MenuItem>
						<MenuItem value={'Negative'}>Negative</MenuItem>
						<MenuItem value={'VeryNegative'}>Very Negative</MenuItem>
					</Select>
				</div>
				<div className="flex flex-col items-center">
					<label>Ratings</label>
					<Rating
						name="simple-controlled"
						value={rating}
						onChange={(event, newRating) => {
							setRating(newRating);
						}}
					/>
				</div>
				<div className="flex items-center space-x-2">
					<Checkbox
						id="autoexp"
						checked={checked}
						onCheckedChange={handleAutoexp}
					/>
					<label>Auto Expantion</label>
				</div>
			</div>
		</form>
	);
};

export default Searchbar;
