export default function TutorialCard({ title, description, category }) {
    return (
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-bold">{title}</h2>
        <p className="text-gray-600">{description}</p>
        <span className="text-sm text-blue-500">{category}</span>
      </div>
    );
  }