const BigButton = ({
  icon,
  buttonLabel,
  eventHandle,
}: {
  icon: any;
  buttonLabel: string;
  eventHandle: any;
}) => {
  return (
    <div>
      <button
        onClick={eventHandle}
        type="button"
        className="bg-[#747474] rounded-[10px] flex flex-col justify-center items-center w-[325px] h-[121px] border-black gap-1
        hover:border-2 hover:border-white border-dashed hover:scale-95"
      >
        {icon}
        <span>{buttonLabel.toLocaleUpperCase()}</span>
      </button>
    </div>
  );
};

export default BigButton;
