import React from 'react';
import { ScrollArea } from '../ui/scroll-area';

const Results = ({ results }) => {
	return (
		<ScrollArea className="w-[90vw] h-[75vh] absolute top-28 bg-gray-200 dark:bg-gray-700 rounded">
			{results.map((restaurant, index) => (
				<div key={index} className="flex flex-col mb-3">
					<div className="flex flex-row">
						<p className="mx-3">{restaurant.resturantName}</p>
						<p className="mx-3">{restaurant.restaurantAddress}</p>
						<p className="mx-3">{restaurant.restaurantStars} Stars</p>
					</div>
					<div className="flex flex-row ml-4">
						<p className="mx-3">{restaurant.reviewText}</p>
						<p className="mx-3">{restaurant.reviewTime}</p>
						<p className="mx-3">{restaurant.reviewStars} Stars</p>
					</div>
				</div>
			))}
		</ScrollArea>
	);
};

export default Results;
