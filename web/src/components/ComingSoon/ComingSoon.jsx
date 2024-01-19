import downloadAppstore from '../../assets/misc/download-appstore.png'
import downloadPlaystore from '../../assets/misc/download-playstore.png'
import background24 from '../../assets/background/24.jpg'

export default function ComingSoon() {
  return (
    <section
      id="section-download"
      className="pt60 pb50 bg-loop text-light overflow-hidden"
      style={{
        backgroundImage: `url(${background24})`,
        backgroundPosition: 'top',
      }}
    >
      <div className="container">
        <div className="row">
          <div className="col-lg-6 text-center wow fadeInLeft">
            <h2>Mobile App Coming Soon</h2>
          </div>
          <div className="col-lg-6 text-center wow fadeInRight">
            <a href="#">
              <img src={downloadAppstore} alt="" />
            </a>
            &nbsp;
            <a href="#">
              <img src={downloadPlaystore} alt="" />
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
