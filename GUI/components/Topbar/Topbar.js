import React from 'react';
import Image from 'next/image';
import { ModeToggle } from '../ToggleDarkLight/ToggleDarkLight';

const Topbar = () => {
	return (
		<div className="flex flex-row w-full justify-center">
			<div className="absolute top-0">
				<Image src="/Logo.png" alt="logo" width={100} height={100} />
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
