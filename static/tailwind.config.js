// tailwind.config = {
//   darkMode: 'class',
//   theme: {
//     extend: {
//       colors: {
//         primary: {"50":"#fff1f2","100":"#ffe4e6","200":"#fecdd3","300":"#fda4af","400":"#fb7185","500":"#f43f5e","600":"#e11d48","700":"#be123c","800":"#9f1239","900":"#881337","950":"#4c0519"}
//       }
//     },
//     fontFamily: {
//       'body': [
//     'Inter', 
//     'ui-sans-serif', 
//     'system-ui', 
//     '-apple-system', 
//     'system-ui', 
//     'Segoe UI', 
//     'Roboto', 
//     'Helvetica Neue', 
//     'Arial', 
//     'Noto Sans', 
//     'sans-serif', 
//     'Apple Color Emoji', 
//     'Segoe UI Emoji', 
//     'Segoe UI Symbol', 
//     'Noto Color Emoji'
//   ],
//       'sans': [
//     'Inter', 
//     'ui-sans-serif', 
//     'system-ui', 
//     '-apple-system', 
//     'system-ui', 
//     'Segoe UI', 
//     'Roboto', 
//     'Helvetica Neue', 
//     'Arial', 
//     'Noto Sans', 
//     'sans-serif', 
//     'Apple Color Emoji', 
//     'Segoe UI Emoji', 
//     'Segoe UI Symbol', 
//     'Noto Color Emoji'
//   ]
//     }
//   }
// }


tailwind.config = {
    darkMode: 'class',
    theme: {
        extend: {
            colors: {
                primary: { "50": "#fff1f2", "100": "#ffe4e6", "200": "#fecdd3", "300": "#fda4af", "400": "#fb7185", "500": "#f43f5e", "600": "#e11d48", "700": "#be123c", "800": "#9f1239", "900": "#881337", "950": "#4c0519" },
                neutral: {
                    'primary-soft': '#f9fafb', // gray-50
                    'secondary-medium': '#e5e7eb', // gray-200
                },
                danger: {
                    DEFAULT: '#ef4444', // red-500
                    medium: '#dc2626', // red-600
                    strong: '#b91c1c', // red-700
                },
                heading: '#111827', // gray-900
                body: '#6b7280', // gray-500
                'fg-brand': '#2563eb', // blue-600
                'border-default': '#e5e7eb', // gray-200
                'shadow-xs': '0 1px 2px 0 rgb(0 0 0 / 0.05)',
                brand: {
                    DEFAULT: '#2563eb', // blue-600
                    medium: '#3b82f6', // blue-500
                    strong: '#1d4ed8', // blue-700
                },
            },
            borderRadius: {
                'base': '0.375rem', // 6px (standard rounded-md)
            }
        },
        fontFamily: {
            'body': [
                'Inter',
                'ui-sans-serif',
                'system-ui',
                '-apple-system',
                'system-ui',
                'Segoe UI',
                'Roboto',
                'Helvetica Neue',
                'Arial',
                'Noto Sans',
                'sans-serif',
                'Apple Color Emoji',
                'Segoe UI Emoji',
                'Segoe UI Symbol',
                'Noto Color Emoji'
            ],
            'sans': [
                'Inter',
                'ui-sans-serif',
                'system-ui',
                '-apple-system',
                'system-ui',
                'Segoe UI',
                'Roboto',
                'Helvetica Neue',
                'Arial',
                'Noto Sans',
                'sans-serif',
                'Apple Color Emoji',
                'Segoe UI Emoji',
                'Segoe UI Symbol',
                'Noto Color Emoji'
            ]
        }
    }
}