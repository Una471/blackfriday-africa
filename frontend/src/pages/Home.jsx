import React, { useState, useEffect } from 'react';
import { getProducts } from '../services/api';
import ProductCard from '../components/ProductCard';
import SearchBar from '../components/SearchBar';

// 1. Import your banner images from their local paths
import banner1Image from '../assets/banner1.png'; // Adjust path as necessary
import banner2Image from '../assets/banner2.jpeg'; // Adjust path as necessary

const homeContainerStyle = {
  maxWidth: '1200px',
  margin: '0 auto',
  padding: '20px',
};

const bannerStyle = {
  backgroundColor: '#333',
  color: 'white',
  padding: '40px 20px',
  textAlign: 'center',
  marginBottom: '20px',
};

const gridContainerStyle = {
  display: 'grid',
  gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
  gap: '20px',
};

// Define style for the image itself within the banner container
const imageStyle = {
  width: '100%',
  height: '100%',
  objectFit: 'cover', // Ensures the image covers the container without distortion
  borderRadius: '10px',
};

const Home = () => {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true);
        const response = await getProducts();
        setProducts(response.data);
        setFilteredProducts(response.data);
      } catch (err) {
        setError('There was an error fetching the products.');
        console.error("Fetch error:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  const handleSearch = ({ searchTerm, minPrice, maxPrice, sortBy, retailer, category }) => {
    let filtered = products.filter((product) =>
      product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    if (minPrice) {
      filtered = filtered.filter((product) => product.price >= parseFloat(minPrice));
    }

    if (maxPrice) {
      filtered = filtered.filter((product) => product.price <= parseFloat(maxPrice));
    }

    if (retailer) {
      filtered = filtered.filter((product) => product.retailer === retailer);
    }

    if (category) {
      filtered = filtered.filter((product) => product.category === category);
    }

    if (sortBy === 'asc') {
      filtered.sort((a, b) => a.price - b.price);
    } else if (sortBy === 'desc') {
      filtered.sort((a, b) => b.price - a.price);
    }

    setFilteredProducts(filtered);
  };

  if (loading) {
    return <div style={{ textAlign: 'center', padding: '50px' }}>Loading products...</div>;
  }

  if (error) {
    return <div style={{ textAlign: 'center', padding: '50px', color: 'red' }}>{error}</div>;
  }

  return (
    <div style={homeContainerStyle}>
      <div style={bannerStyle}>
        <h1>Black Friday Deals</h1>
        <p>Your one-stop shop for the best deals in Africa.</p>
      </div>

      <div style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))",
        gap: "20px",
        marginBottom: "30px"
      }}>
        {/* 2. Replace placeholder div with an <img> tag for Banner 1 */}
        <div style={{
          height: "150px",
          borderRadius: "10px",
          overflow: "hidden", // Important to contain the image within the border radius
          // Removed placeholder background/text styles
        }}>
          <img
            src={banner1Image}
            alt="Promotional Banner 1"
            style={imageStyle}
          />
        </div>

        {/* 3. Replace placeholder div with an <img> tag for Banner 2 */}
        <div style={{
          height: "150px",
          borderRadius: "10px",
          overflow: "hidden", // Important to contain the image within the border radius
          // Removed placeholder background/text styles
        }}>
          <img
            src={banner2Image}
            alt="Promotional Banner 2"
            style={imageStyle}
          />
        </div>
      </div>

      <SearchBar onSearch={handleSearch} />

      {filteredProducts.length > 0 ? (
        <div style={gridContainerStyle}>
          {filteredProducts.map((product) => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      ) : (
        <div style={{ textAlign: 'center', padding: '50px' }}>No products found.</div>
      )}
    </div>
  );
};

export default Home;