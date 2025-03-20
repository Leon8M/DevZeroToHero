import { useEffect, useState } from "react";
import TutorialCard from "../components/TutorialCard";

export default function Tutorials() {
  const [tutorials, setTutorials] = useState([]);

  useEffect(() => {
    fetch("/api/tutorials")
      .then((response) => response.json())
      .then((data) => setTutorials(data));
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Tutorials</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {tutorials.map((tutorial) => (
          <TutorialCard
            key={tutorial._id}
            title={tutorial.title}
            description={tutorial.description}
            category={tutorial.category}
          />
        ))}
      </div>
    </div>
  );
}