import Header from '../Header/Header';
import Footer from '../Footer/Footer';

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen">
      <div className="flex flex-1 flex-col">
        <Header />
        <main className="flex-1 p-6 overflow-y-auto">
            {children}
        </main>
        <Footer/>
      </div>
    </div>
  );
}
