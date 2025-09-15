export const RESUME_DATA = {
  name: "Nguyen Bao Ngoc",
  initials: "NBN",
  location: "Ho Chi Minh City, Vietnam",
  locationLink: "https://maps.google.com/?q=Ho%20Chi%20Minh%20City",
  about:
    "Final-year student in Investment Economics (UEH) aiming for a career in banking & finance. Strong fundamentals in project appraisal, corporate finance, and capital markets. Internship experience at ACB with customer operations and basic data analysis. Proficient with Excel/Power BI; Python & SQL for quantitative tasks.",
  summary:
    "Investment Economics student passionate about banking & finance. I enjoy turning financial and business data into clear insights and decisions.",

  avatarUrl: "", // optional: add a link to your avatar if you have one
  personalWebsiteUrl: "",

  contact: {
    email: "nnguyenbao400@gmail.com",
    tel: "+84398780027",
    social: [
      { name: "LinkedIn", url: "https://www.linkedin.com/in/BaoNgoc27" },
      { name: "GitHub", url: "https://github.com/BaoNgoc27" },
    ],
  },

  education: [
    {
      school: "University of Economics Ho Chi Minh City (UEH)",
      degree: "B.A. in Investment Economics",
      start: "2021-09",
      end: "Present",
      location: "Ho Chi Minh City, Vietnam",
      GPA: "3.5/4.0 (expected 2025)",
      courses: [
        "Investment Project Appraisal",
        "Asset Valuation",
        "Corporate Finance",
        "Capital Markets",
      ],
      highlights: [
        "Member of Finance & Banking Club; case studies and academic workshops.",
      ],
    },
  ],

  work: [
    {
      company: "Asia Commercial Bank (ACB)",
      link: "https://www.acb.com.vn",
      title: "Intern — Retail Banking",
      start: "2024-06",
      end: "2024-08",
      location: "Ho Chi Minh City, Vietnam",
      badges: ["Branch Ops", "Customer Service"],
      description:
        "Supported counter transactions (account opening, deposits, cards). Conducted basic customer data analysis to assist loyalty care. Learned credit workflow and helped prepare personal loan documents.",
      highlights: [
        "Praised for responsibility, communication and teamwork.",
      ],
    },
  ],

  projects: [
    {
      title: "Investment Project Feasibility Analysis",
      techStack: ["Excel"],
      start: "2023-09",
      end: "2023-12",
      description:
        "Evaluated infrastructure project feasibility using NPV, IRR and Payback. Built Excel model & report; produced policy and investment recommendations.",
      links: [],
    },
    {
      title: "Retail Sales Data Analysis",
      techStack: ["Python", "Pandas", "Matplotlib", "Seaborn", "Power BI"],
      start: "2024-01",
      end: "2024-03",
      description:
        "Explored sales data, built visuals and KPIs dashboards; proposed actionable business suggestions.",
      links: [],
    },
    {
      title: "Student Management Web App",
      techStack: ["React", "Node.js", "Express", "MySQL"],
      start: "2023-05",
      end: "2023-07",
      description:
        "CRUD app for student records and reports. Course project graded 95/100.",
      links: [
        { title: "GitHub", href: "https://github.com/BaoNgoc27/student-management" },
      ],
    },
  ],

  skills: [
    {
      name: "Banking & Finance",
      keywords: [
        "Financial statement analysis",
        "Credit workflow",
        "Deposit & lending products",
      ],
    },
    {
      name: "Investment Economics",
      keywords: [
        "Project appraisal (NPV/IRR/Payback)",
        "Asset valuation",
        "Capital markets",
      ],
    },
    {
      name: "Data & Tools",
      keywords: [
        "Excel (advanced)",
        "Power BI",
        "Python (Pandas/Matplotlib)",
        "SQL",
      ],
    },
    {
      name: "Soft Skills",
      keywords: ["Communication", "Teamwork", "Time management", "Analytical thinking"],
    },
  ],

  languages: [
    { name: "Vietnamese", level: "Native" },
    { name: "English", level: "Intermediate (IELTS 6.0)" },
  ],

  certifications: [
    // Add items if you have any, e.g. { name: "Bloomberg Market Concepts (BMC)", issuer: "Bloomberg", year: "2024" }
  ],
} as const;

export default RESUME_DATA;
