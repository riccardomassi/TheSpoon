import SearchEngine from '@/components/SearchEngine/SearchEngine';
import Topbar from '@/components/Topbar/Topbar';

export default function Home() {
	return (
		<div className="flex flex-col w-screen h-screen bg-slate-100 dark:bg-slate-800 items-center justify-center">
			<SearchEngine />
			<Topbar />
		</div>
	);
}
