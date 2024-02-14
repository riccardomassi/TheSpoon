import { React, useState, useEffect } from 'react';
import { ScrollArea } from '../ui/scroll-area';

const Results = ({ results, error }) => {
	// Function to format the reviewTime
	const formatReviewTime = (rawTime) => {
		const date = new Date(rawTime);
		// Formatting the date as "Day, DD Mon YYYY"
		const formattedTime = date.toLocaleString('en-US', {
			weekday: 'short',
			day: 'numeric',
			month: 'short',
			year: 'numeric',
		});

		return formattedTime;
	};

	return (
		<ScrollArea className="w-[90vw] h-[75vh] absolute top-28 bg-gray-200 dark:bg-gray-700 rounded">
			{!error &&
				results.map((restaurant, index) => (
					<div key={index}>
						<div className="flex flex-col mb-6">
							<h1 className="flex text-xl justify-center">RESTAURANT</h1>
							<div className="flex flex-row justify-center">
								<p className="mx-5">{restaurant.resturantName}</p>
								<p className="mx-5">{restaurant.restaurantAddress}</p>
								<p className="mx-5">{restaurant.restaurantStars} ★</p>
							</div>
						</div>
						<div className="mb-6">
							<div className="flex flex-col items-center">
								<h1 className="flex w-full text-xl justify-center">REVIEW</h1>
								<p className="text-center">{restaurant.reviewText}</p>
								<div className="flex flex-row justify-between mt-2">
									<p className="mx-5">
										{formatReviewTime(restaurant.reviewTime)}
									</p>
									<p className="mx-5">{restaurant.reviewStars} ★</p>
								</div>
							</div>
						</div>
						<div className="border-t border-gray-800 dark:border-gray-300 my-4"></div>
					</div>
				))}
			{error && (
				<div className="flex justify-center">
					<div className="bg-yellow-300 py-20 w-1/2 rounded text-4xl text-black mt-48 flex flex-col items-center">
						<p className="mb-4">No match found!</p>
						<p>Try enabling Auto Expansion?</p>
					</div>
				</div>
			)}
		</ScrollArea>
	);
};

export default Results;
