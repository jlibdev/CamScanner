import axios from "axios";
import { Aperture, HomeIcon } from "lucide-react";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const CapturePage = () => {
  const [cameraStatus, setCameraStatus] = useState("loading");
  function handleStartCamera() {
    axios
      .get("http://127.0.0.1:8000/start_cam/")
      .then((res) => setCameraStatus(res.data.status))
      .catch((err) => {
        console.error(err);
        setCameraStatus("error");
      });
  }

  function handleStopCamera() {
    setCameraStatus("Stopped");
    axios.get("http://127.0.0.1:8000/stop_cam/").then(() => {
      setCameraStatus("Stopped");
    });
  }

  useEffect(() => {
    handleStartCamera();
  }, []);

  return (
    <div className="w-screen h-screen flex flex-col overflow-hidden">
      <section className="p-2">
        <Link
          to="/"
          className="p-2 rounded-full hover:bg-[#ACACAC] w-fit flex"
          onClick={handleStopCamera}
        >
          <HomeIcon color="white" />
        </Link>
      </section>
      <section className="flex flex-col items-center gap-5">
        <section className="bg-[#ACACAC] w-[960px] h-[720px] rounded-[10px] justify-center flex relative">
          {cameraStatus === "Success" || cameraStatus === "Already running" ? (
            <img
              src="http://127.0.0.1:8000/video_feed/"
              className="h-full rounded-[10px]"
            />
          ) : cameraStatus === "loading" ? (
            <div className="text-yellow-500 font-semibold text-lg">
              🟡 Starting camera...
            </div>
          ) : (
            <div className="text-red-500 font-semibold text-lg">
              🔴 Camera unavailable
            </div>
          )}

          <button className="absolute bottom-5 rounded-full border-4 p-2 hover:bg-gray-300 transition-all">
            <Aperture size={75} strokeWidth={1} className="hover:scale-125" />
          </button>
        </section>
      </section>
    </div>
  );
};

export default CapturePage;
