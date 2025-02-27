import { Camera, FolderDown } from "lucide-react";
import BigButton from "../components/BigButton";

const LandingPage = () => {
  function handleImportClick() {
    console.log("import");
  }
  return (
    <div className="font-[Jura] w-screen h-screen p-5 overflow-hidden">
      <section className="flex w-full justify-center items-center flex-col">
        <p className="text-7xl">CAMSCAMMER</p>
        <section className="grid grid-cols-2 gap-20 mt-10">
          <BigButton
            link="/"
            icon={<FolderDown />}
            buttonLabel="import image from local storage"
            eventHandle={handleImportClick}
          />
          <BigButton
            link="/capture"
            icon={<Camera />}
            buttonLabel="capture image from camera"
            eventHandle={handleImportClick}
          />
        </section>
      </section>
      <section className="p-10 flex flex-col">
        <p>FILE STREAM</p>
        <section className="grid grid-cols-2 gap-2 bg-[#747474] w-full h-[400px] rounded-[10px] p-2 ">
          <section className="bg-[#D1D1D1] rounded-[5px] p-2 text-black">
            <p>IMAGES</p>
          </section>
          <section className="bg-[#D1D1D1] rounded-[5px] p-2 text-black">
            <p>PDF</p>
          </section>
        </section>
      </section>
    </div>
  );
};

export default LandingPage;
