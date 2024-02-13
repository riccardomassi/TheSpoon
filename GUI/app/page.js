import SearchEnginePage from './SearchEngine/page';

export default function Home() {
	return (
		<div className="text-4xl flex w-screen h-screen bg-slate-100 dark:bg-slate-800 flex-auto items-center justify-center">
			<SearchEnginePage />
		</div>
	);
}
