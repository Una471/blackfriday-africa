import React, { useState, useEffect } from "react";
import { getRetailers, getCategories } from "../services/api";

const SearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [minPrice, setMinPrice] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [sortBy, setSortBy] = useState("");
  const [retailer, setRetailer] = useState("");
  const [category, setCategory] = useState("");

  const [retailers, setRetailers] = useState([]);
  const [categories, setCategories] = useState([]);
  const [advancedOpen, setAdvancedOpen] = useState(false);

  useEffect(() => {
    const loadFilters = async () => {
      const r = await getRetailers();
      const c = await getCategories();

      setRetailers(r.data);
      setCategories(c.data);
    };

    loadFilters();
  }, []);

  const applyFilters = () => {
    onSearch({ searchTerm, minPrice, maxPrice, sortBy, retailer, category });
  };

  const clearFilters = () => {
    setSearchTerm("");
    setMinPrice("");
    setMaxPrice("");
    setSortBy("");
    setRetailer("");
    setCategory("");
    onSearch({ searchTerm: "", minPrice: "", maxPrice: "", sortBy: "", retailer: "", category: "" });
  };

  return (
    <div className="bg-white shadow-md p-5 rounded-xl mb-6">
      {/* Search Box */}
      <div className="flex gap-3 items-center">
        <input
          type="text"
          placeholder="Search products..."
          className="w-full border rounded-lg px-4 py-2"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        <button
          onClick={applyFilters}
          className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Search
        </button>

        <button
          onClick={clearFilters}
          className="px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition"
        >
          Clear
        </button>
      </div>

      {/* Toggle Advanced Filters */}
      <p
        className="mt-3 text-blue-600 cursor-pointer text-sm"
        onClick={() => setAdvancedOpen(!advancedOpen)}
      >
        {advancedOpen ? "Hide Advanced Filters ▲" : "Show Advanced Filters ▼"}
      </p>

      {/* Advanced Section */}
      {advancedOpen && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-5">
          <input
            type="number"
            placeholder="Min Price"
            className="border rounded-lg px-4 py-2"
            value={minPrice}
            onChange={(e) => setMinPrice(e.target.value)}
          />

          <input
            type="number"
            placeholder="Max Price"
            className="border rounded-lg px-4 py-2"
            value={maxPrice}
            onChange={(e) => setMaxPrice(e.target.value)}
          />

          <select
            className="border rounded-lg px-4 py-2"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="">Sort By</option>
            <option value="asc">Price: Low → High</option>
            <option value="desc">Price: High → Low</option>
          </select>

          <select
            className="border rounded-lg px-4 py-2"
            value={retailer}
            onChange={(e) => setRetailer(e.target.value)}
          >
            <option value="">Retailer</option>
            {retailers.map((r) => (
              <option key={r} value={r}>
                {r}
              </option>
            ))}
          </select>

          <select
            className="border rounded-lg px-4 py-2"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          >
            <option value="">Category</option>
            {categories.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </div>
      )}
    </div>
  );
};

export default SearchBar;
