*Greetings from, I,* **[Knoph Ayieko](https://github.com/Knoph1)** 👋

<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYndwd2dlYThvczl0ZXc3cjduMzNjZ3lyNnljZnpldDdsM2IwdTdieCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jBOOXxSJfG8kqMxT11/giphy.gif" height="210">

> *Welcome to my *GitHub* profile*

---

## 📈 GitHub Stats

<div align="flex">

  <!-- GitHub Stats with "contribs" hidden -->
  <img src="https://github-readme-stats.vercel.app/api?username=Knoph1&show_icons=true&theme=compact&hide=contribs" />
  <!-- Top Languages -->
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Knoph1&layout=compact&theme=compact" />

</div>

---

---

# 📊 Animated Chart Demo

This project demonstrates a **motion-slide animated chart** built with **React + Recharts + Framer Motion**.

---

## 🚀 Demo Preview
![Chart Animation](assets/chart-demo.gif)

[🔗 Live Demo](https://knoph.dev/chart-demo)

---

## 🛠️ Code Example

```jsx
import { motion } from "framer-motion";
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from "recharts";

const data = [
  { name: "Jan", value: 40 },
  { name: "Feb", value: 80 },
  { name: "Mar", value: 60 },
  { name: "Apr", value: 100 },
];

export default function AnimatedChart() {
  return (
    <motion.div
      initial={{ opacity: 0, x: -100 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 1 }}
    >
      <LineChart width={500} height={300} data={data}>
        <CartesianGrid stroke="#ccc" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="value" stroke="#007bff" strokeWidth={3} />
      </LineChart>
    </motion.div>
  );
}
```

m

## 📈 GitHub Stats

<!-- Animated Showcase (GIF preview of sliding charts) -->
<p align="center">
  <img src="assets/github-stats-animated.gif" alt="GitHub Stats Animation" width="80%">
</p>

---

<!-- Interactive Reveal (click-to-show effect) -->
<details>
  <summary>✨ Click to reveal live stats</summary>
  <div align="center">

  <!-- GitHub Stats with "contribs" hidden -->
  <img src="https://github-readme-stats.vercel.app/api?username=Knoph1&show_icons=true&theme=compact&hide=contribs" />

  <!-- Top Languages -->
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Knoph1&layout=compact&theme=compact" />

  </div>
</details>

---

### 🔗 Live Animated Demo
You can see the full animated motion-slide chart here:  
👉 [View Live Demo](https://your-live-demo-link.com)


---

## 💖 Sponsor My Work

I’m building impactful, open-source tech and educational tools across Africa to the globe.

Your sponsorship helps me:
- Build free, accessible digital platforms and resources for learning and small businesses
- Contribute to public projects that serve under-served communities
- Aid **O.L Foundation** to train, mentor and uplift the next generation of devs

Whether it’s a ☕ coffee and/or a strategic partnership, **you are fueling purpose and progress.**

[![Sponsor Me](https://img.shields.io/badge/Sponsor-Knoph%20Ayieko-%23ff69b4?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/Knoph1)

Thank you in-advance for supporting African tech and dreams that matter! 🌍🚀

---

![Web App Developer](https://img.shields.io/badge/Developed%20By%20%3A-Knoph%20Ayieko)

### [Knoph Ayieko](https://github.com/Knoph1)

_Official Portfolio:_ **[knoph.dev](https://www.knoph.dev/)**

[![GitHub Followers](https://img.shields.io/github/followers/Knoph1?style=social)](https://github.com/Knoph1)
[![GitHub Stars](https://img.shields.io/github/stars/Knoph1?style=social)](https://github.com/Knoph1)
[![Website](https://img.shields.io/badge/Website-knoph.dev-blue?style=flat&logo=google-chrome)](https://knoph.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Knoph%20Ayieko-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/knoph-ayieko)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--3787--513X-green?style=flat&logo=orcid)](https://orcid.org/0009-0001-3787-513X)

---

**Thanks for visiting my GitHub profile, feel free to explore and collaborate.**

<!-- Footer closure --!>

<div style="display: flex; align-items: left; gap: 16px;">

  <!-- Paragraphs aligned to the left of the icon -->
  <div style="display: flex; flex-direction: column; justify-content: center;">
    <p style="margin: 0; font-style: italic;">Build for people. Code with purpose. Collaborate for impact.</p>
    <p style="margin: 0; font-weight: bold;">&copy; 2025 | Knoph Ayieko</p>
  </div>

   <!-- GitHub Icon -->
  <a href="https://github.com/Knoph1" target="_blank" rel="noopener noreferrer">
    <img src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="GitHub" height="40">
  </a>

</div>
