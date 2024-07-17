import React, { useState, useRef, useEffect } from 'react';

const Results = ({ results, error }) => {
	const [currentPage, setCurrentPage] = useState(1);
	const itemsPerPage = 10;
	const scrollRef = useRef(null);

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

	// Calculate the index range for the current page
	const indexOfLastItem = currentPage * itemsPerPage;
	const indexOfFirstItem = indexOfLastItem - itemsPerPage;
	const currentItems = results.slice(indexOfFirstItem, indexOfLastItem);

	// Function to handle page changes
	const handlePageChange = (pageNumber) => {
		setCurrentPage(pageNumber);
	};

	// Effetto per eseguire lo scroll al cambiamento di pagina
	useEffect(() => {
		scrollRef.current.scrollTo({
			top: 0,
			behavior: 'smooth',
		});

	}, [currentPage]);

	// Calculate the total number of pages
	const totalPages = Math.ceil(results.length / itemsPerPage);

	return (
		<div className={`absolute ${error ? "top-72" : "top-52"} bg-gray-100 dark:bg-gray-800 rounded-lg p-4 shadow-lg`}>
			{!error && (
				<>
					<div ref={scrollRef} className="h-[63vh] w-[90vw] overflow-y-scroll mb-4">
						{currentItems.map((restaurant, index) => (
							<div key={index} className="bg-white dark:bg-gray-900 p-6 mb-6 rounded-lg shadow-md">
								<div className="mb-4">
									<h1 className="text-2xl font-bold text-center text-gray-800 dark:text-gray-200">RESTAURANT</h1>
									<div className="text-center">
										<p className="text-lg font-semibold text-gray-700 dark:text-gray-300">{restaurant.resturantName}</p>
										<p className="text-gray-600 dark:text-gray-400">{restaurant.restaurantAddress}</p>
										<p className="text-yellow-500">{restaurant.restaurantStars} ★</p>
									</div>
								</div>
								<div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
									<h2 className="text-xl font-bold text-center text-gray-800 dark:text-gray-200">REVIEW</h2>
									<p className="text-gray-700 dark:text-gray-300 my-2">{restaurant.reviewText}</p>
									<div className="flex justify-between items-center mt-4">
										<p className="text-gray-600 dark:text-gray-400">{formatReviewTime(restaurant.reviewTime)}</p>
										<p className="text-yellow-500">{restaurant.reviewStars} ★</p>
									</div>
								</div>
							</div>
						))}
					</div>
					<div className="flex justify-center mt-2">
						{Array.from({ length: totalPages }, (_, index) => (
							<button
								key={index}
								onClick={() => handlePageChange(index + 1)}
								className={`px-4 py-2 mx-1 rounded-lg ${currentPage === index + 1
									? 'bg-blue-500 text-white'
									: 'bg-gray-300 text-gray-800 dark:bg-gray-700 dark:text-gray-200'
									}`}
							>
								{index + 1}
							</button>
						))}
					</div>
				</>
			)}
			{error && (
				<div className="flex justify-center">
					<div className="bg-yellow-300 p-10 rounded text-4xl text-black flex flex-col items-center">
						<p className="mb-4">No match found!</p>
						<p>Try enabling Auto Expansion?</p>
					</div>
				</div>
			)}
		</div>
	);
};

export default Results;
