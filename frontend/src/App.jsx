import React, { useEffect, useState } from 'react';
import { Link, Outlet } from 'react-router-dom';
import { getRetailers, getCategories } from "./services/api";
import './App.css';

function App() {
  const [retailers, setRetailers] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const load = async () => {
      try {
        const r = await getRetailers();
        const c = await getCategories();

        setRetailers(r.data);
        setCategories(c.data);
      } catch (err) {
        console.error("Navbar fetch error:", err);
      }
    };

    load();
  }, []);

  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-content">
          <Link to="/" className="nav-logo">BlackFriday Deals</Link>

          <div className="nav-links">
            <Link to="/" className="nav-link">Home</Link>

            {/* Dynamic Categories */}
            <div className="dropdown">
              <button className="dropbtn">Categories</button>
              <div className="dropdown-content">
                {categories.length === 0 ? (
                  <span>No Categories</span>
                ) : (
                  categories.map(c => (
                    <Link key={c} to={`/category/${c.toLowerCase()}`}>{c}</Link>
                  ))
                )}
              </div>
            </div>

            {/* Dynamic Retailers */}
            <div className="dropdown">
              <button className="dropbtn">Retailers</button>
              <div className="dropdown-content">
                {retailers.length === 0 ? (
                  <span>No Retailers</span>
                ) : (
                  retailers.map(r => (
                    <Link key={r} to={`/retailer/${r.toLowerCase()}`}>{r}</Link>
                  ))
                )}
              </div>
            </div>
          </div>
        </div>
      </nav>

      <main className="main-content">
        <Outlet />
      </main>

      <footer className="footer">
        <p>&copy; 2025 BlackFriday Deals. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
