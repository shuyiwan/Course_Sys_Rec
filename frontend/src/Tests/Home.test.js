import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import Home from '../Pages/Home.js';
import { BrowserRouter } from 'react-router-dom'; 
import { act } from 'react-dom/test-utils'; 

// Mock the useHistory hook to mock navigation
jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useHistory: jest.fn(),
}));

describe('HomePage', () => {
  it('should navigate to the search page when user enters a keyword and presses Enter', async () => {
    // Render the HomePage component
    const { getByPlaceholderText } = render(
      <BrowserRouter>
        <Home />
      </BrowserRouter>
    );

    // Simulate user entering a keyword in the search input
    const input = getByPlaceholderText('Search for courses');
    fireEvent.change(input, { target: { value: 'algorithms' } });

    // Trigger the search action (e.g., by pressing Enter)
    fireEvent.keyDown(input, { key: 'Enter', code: 'Enter' });

    // Assert that navigation to the search page is triggered with the correct URL
    act(() => {});
    const currentUrl = window.location.pathname;
    expect(currentUrl).toBe('/search');
  });

});
