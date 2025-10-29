# Changelog

## [Unreleased] - 2025-10-29

### Changed
- Complete redesign of index.html with modern Klippa.io-inspired layout
- Added minimal header with logo and navigation links
- Created hero section with large headline and subtitle
- Implemented two-mode toggle buttons (Gamma watermark / Other watermark)
- Added large drag-and-drop upload zone in center of hero
- Added three feature cards with icons below hero section
- Separated CSS to external stylesheet (styles.css)
- Separated JavaScript to external file (main.js)
- Added responsive design structure for mobile compatibility
- Implemented clean color accent scheme matching reference design

### Added
- Complete CSS styling with dark gradient background (#0a1929 to #1a2942)
- Blue accent color (#00d4ff) throughout the design
- Interactive drag-and-drop functionality for file uploads
- Hover effects and transitions on all interactive elements
- Mode toggle functionality for switching between watermark types
- Responsive breakpoints for mobile devices (768px)
- Fixed header with backdrop blur effect
- Feature cards with icon backgrounds and hover animations

### Fixed
- Updated FastAPI template directory path from "templates" to "app/templates"
- Added StaticFiles mount for serving CSS and JavaScript files
- Imported fastapi.staticfiles.StaticFiles to enable static file serving
