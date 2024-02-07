import React from 'react';
import Link from 'next/link';
import { ModeToggle } from '@/components/ToggleDarkLight/ToggleDarkLight';

const Navbar = () => {
	return (
		<div className="bg-slate-300 dark:bg-slate-900 fixed w-full top-0 shadow-xl">
			<div className="container flex items-center justify-between">
				<Link href="/Presentation">Presentation</Link>
				<Link href="/SearchEngine">Search Engine</Link>
				<ModeToggle />
			</div>
		</div>
	);
};

export default Navbar;
