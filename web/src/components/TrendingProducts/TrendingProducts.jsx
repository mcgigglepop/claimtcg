import crs13 from '../../assets/carousel/crs-13.jpg'
import crs12 from '../../assets/carousel/crs-12.jpg'
import crs16 from '../../assets/carousel/crs-16.jpg'
import crs17 from '../../assets/carousel/crs-17.jpg'
import crs15 from '../../assets/carousel/crs-15.jpg'
import crs14 from '../../assets/carousel/crs-14.jpg'

export default function TrendingProducts() {
  return (
    <section
      id="section-trending-projects"
      className="no-top no-bottom position-relative"
    >
      <div className="container-fluid">
        <div className="row">
          <div className="col-md-12 mt-100">
            <div className="d-carousel">
              <div
                id="item-carousel-big-type-4"
                className="owl-carousel owl-center"
                data-wow-delay="1s"
              >
                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">
                        First Edition Charizard
                      </span>
                      <span className="nft_pic_by">PSA 10</span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs13} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>

                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">
                        Blue-Eyes White Dragon
                      </span>
                      <span className="nft_pic_by">PSA 10</span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs12} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>

                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">Pikachu Illustrator</span>
                      <span className="nft_pic_by">PSA 9</span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs16} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>

                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">
                        Legend of Blue-Eyes White Dragon
                      </span>
                      <span className="nft_pic_by">
                        1st Edition Booster Box
                      </span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs17} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>

                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">
                        Family Event Trophy Kangaskhan
                      </span>
                      <span className="nft_pic_by">PSA 10</span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs15} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>

                <div className="nft_pic mod-b">
                  <a href="#">
                    <span className="nft_pic_info">
                      <span className="nft_pic_title">Pokemon Base Set</span>
                      <span className="nft_pic_by">
                        1st Edition Booster Box
                      </span>
                    </span>

                    <div className="nft_pic_wrap">
                      <img src={crs14} className="lazy img-fluid" alt="" />
                    </div>
                  </a>
                </div>
              </div>
              <div className="d-arrow-left mod-a">
                <i className="fa fa-angle-left"></i>
              </div>
              <div className="d-arrow-right mod-a">
                <i className="fa fa-angle-right"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
