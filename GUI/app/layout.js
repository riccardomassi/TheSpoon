import './globals.css';
import { ThemeProvider } from '@/components/ToggleDarkLight/ThemeProvider';

export const metadata = {
	title: 'The Spoon',
	description: '',
};

export default function RootLayout({ children }) {
	return (
		<html lang="en">
			<body className="flex fixed flex-row h-full w-full">
				<ThemeProvider
					attribute="class"
					defaultTheme="system"
					enableSystem
					disableTransitionOnChange
				>
					<main>{children}</main>
				</ThemeProvider>
			</body>
		</html>
	);
}
