'use client';
import { React, useEffect, useState } from 'react';
import Image from 'next/image';
import { ModeToggle } from '../ToggleDarkLight/ToggleDarkLight';
import { useTheme } from 'next-themes';

const Topbar = () => {
	const { theme } = useTheme();
	const [mode, setMode] = useState('dark');
	useEffect(() => {
		setMode(theme);
	}, [theme]);
	const getImagePath = () => {
		return `/${mode}/${mode}-mode-logo.png`;
	};

	return (
		<div className="flex flex-row w-full justify-center">
			<div className="absolute top-0">
				<Image src={getImagePath()} alt="logo" width={100} height={100} />
			</div>
			<div>
				<div className="absolute top-0 right-0 p-2">
					<ModeToggle />
				</div>
			</div>
		</div>
	);
};

export default Topbar;
