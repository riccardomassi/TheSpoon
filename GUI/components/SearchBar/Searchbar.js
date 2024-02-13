'use client';
import { React, useState } from 'react';
import { Search, ChevronDown } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Checkbox } from '../ui/checkbox';
import {
	DropdownMenu,
	DropdownMenuCheckboxItem,
	DropdownMenuContent,
	DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { Rating } from '@mui/material';

const Searchbar = () => {
	const [rating, setRating] = useState(1);
	const [checked, setChecked] = useState(false);
	const [showStatusBar, setShowStatusBar] = useState(true);
	const [showActivityBar, setShowActivityBar] = useState(false);
	const [showPanel, setShowPanel] = useState(false);

	const handleChange = (event) => {
		setChecked(event);
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
					<DropdownMenu>
						<DropdownMenuTrigger asChild>
							<Button variant="default">
								<div className="flex flex-row items-center">
									<div className="mr-2">Sentiments</div>
									<ChevronDown />
								</div>
							</Button>
						</DropdownMenuTrigger>
						<DropdownMenuContent className="w-56">
							<DropdownMenuCheckboxItem
								checked={showStatusBar}
								onCheckedChange={setShowStatusBar}
							>
								Status Bar
							</DropdownMenuCheckboxItem>
							<DropdownMenuCheckboxItem
								checked={showActivityBar}
								onCheckedChange={setShowActivityBar}
							>
								Activity Bar
							</DropdownMenuCheckboxItem>
							<DropdownMenuCheckboxItem
								checked={showPanel}
								onCheckedChange={setShowPanel}
							>
								Panel
							</DropdownMenuCheckboxItem>
						</DropdownMenuContent>
					</DropdownMenu>
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
						onCheckedChange={handleChange}
					/>
					<label>Auto Expantion</label>
				</div>
			</div>
		</form>
	);
};

export default Searchbar;
