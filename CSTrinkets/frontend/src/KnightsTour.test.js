import { render, screen } from '@testing-library/react';
import KnightsTour from './KnightsTour';

test('renders learn react link', () => {
  render(<KnightsTour />);
  const linkElement = screen.getByText(/KnightsTour/i);
  expect(linkElement).toBeInTheDocument();
});
