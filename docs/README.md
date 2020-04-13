# InnopolisAIArt
Given an 512x512 image, creates an art (another similar 512x512 image) via evolutionary algorithm
An assignment on Introduction to AI Spring 2020 (2nd year) course in Innopolis University



## General information

* The code was implemented, tested and is expected to work in `Python 3.7.7`
* To use the code, put the input image in the same directory as the `.py` file and name it `input.png`. The output will be saved as
`output.png`
* You can also change input/output file paths by changing constants in the code
* Script can produce gifs showing progress of EA and comparison with original image (see below for examples)
* [The pdf report](report.pdf)



## Examples of produced arts

More examples be found [here](https://yadi.sk/d/ksCLVsqO1F-Gww)
Also, you can find all animated collages at one page [here](https://imgur.com/gallery/dHTWSKw).

<p align="center">
  <img width=300 src="https://s197vla.storage.yandex.net/rdisk/372a4cd6342094d4f930952144d7c8968ef894f2c634102e60c606b9bbf3a435/5e936bf8/bdoooSi8U1bZWHDWmel2x8C5QyUkCu7-NWJw1QuSSKck6cJIOQiRloNrlaqGrfFYuRACx2P98J2TKggjpuGiMw==?uid=293684676&filename=2input.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&hid=745a9225121a7596d1cb20ce2468cf8e&fsize=542502&etag=c60b76f8de61f82e042370e2ae6b81c0&media_type=image&rtoken=P2SMMUWOMyZa&force_default=yes&ycrid=na-5a3255bfa1a86e73ff487b3808fb8ce4-downloader7e&ts=5a31cfa38ee00&s=2925407292cccecb166942980421b08858504f5583c727fd4848ba7e458ab2c1&pb=U2FsdGVkX18LJRGAOJrKiEilnEfhhWLycqWhnc1agVfOmkLux7g-VxWjRQfoKZBf1vBtBNOugwJkz2Jt97BRwonYSIMiAJnCqhQKkucTgQY">
  <img width=300 src="https://s78iva.storage.yandex.net/rdisk/0d045edf80414db9ea511f66cc4fd8393fdd9762ff415bc26fa353b45615117a/5e936c05/bdoooSi8U1bZWHDWmel2x_ro3R_Jobmeg6-sdS8pzLmFzG5tjbHOD9p7s8Q0nyUSTDsc_2Ad3RKzdrY1QgUKZw==?uid=293684676&filename=2output.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&fsize=376948&hid=42022f712deeb7a6e6af6ebedb1ad2b1&media_type=image&etag=41d302f690837ae3d1d1aceaa00fff1f&rtoken=vvFj4Tf0Z8HC&force_default=yes&ycrid=na-edf6cfc083045fe57c121bf2e9479240-downloader7e&ts=5a31cfaff4b40&s=b0c73c21cc34877a056dc172c9136c6b94145136f1dad8f82b448a73cc88e2e4&pb=U2FsdGVkX1_nQ4KUWdTIPgDtDxEy5ACckxZNZrI2KwFrEW3uvNzIS5i9rsKAKN5XzfTsVeesFichn12FTYC0rwClrrPZxRPdRzS_1ASZlxo">
  <br>
  Life is Strange / <a href="https://i.imgur.com/I8vew9z.gifv">view animated version</a><br>
</p>
<p align="center">
  <img width=300 src="https://s576sas.storage.yandex.net/rdisk/8abe01bb6befd8661e0a4d67606cf35b4fd05d978ac02641248ffb7b99a6cb38/5e937830/bdoooSi8U1bZWHDWmel2xxsccQ9Upyg_qeAVaGR8q_ri9lm_ebs1Rv-5caaeu6E09MGZajgiBlvIj9VHwmdjBA==?uid=293684676&filename=6input.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&hid=998b578f81cdc86b5cf5f15fbbef10a5&fsize=644481&media_type=image&etag=47beee500bdfb7dcc297cd85db2c0acb&rtoken=Bn0PazcdxWzC&force_default=yes&ycrid=na-38b30b62739e2d525f724b2a537a8d0c-downloader4e&ts=5a31db4aa6c00&s=0753f29540f0cdb914b5b1589160ce159c3e460a43fabc2099c20341409918b9&pb=U2FsdGVkX191JpDg27Xq3Al0eP9fY6I2AFJyFX98B8gCSJe2EIFUuBmcGiMoNyCpzt3lLBmbkSR-wMBjD0mTm0DJHZteVRlu99FVBEUOWOc">
  <img width=300 src="https://s171iva.storage.yandex.net/rdisk/0ea9f8f32ab0390c22d6edcec33f32a07543de577ef159d79b83e1966872b6ea/5e937847/bdoooSi8U1bZWHDWmel2x2xXnUhbyC-q7GOq4TThpLSPps0a8PnZaI3Gv2XuoV1jMiWrMUQi3nfokaMAJtAWuA==?uid=293684676&filename=6output.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&hid=474a42b8a30fd652042c32421d20e303&media_type=image&etag=0f6571ebc63ea83416e6c93a246a58fd&fsize=424186&rtoken=FDgr03DNo0vf&force_default=yes&ycrid=na-ef029df4b702ecd66cb952bc28d09e32-downloader4e&ts=5a31db6095fc0&s=a0110e9b892d5e3542fe946506d927a08b44acd9511440641f4d128786f03ceb&pb=U2FsdGVkX18yXG8X1_4iYOeUN56PnsVNQWgHGhG8Jcn0qbYb1YcxxxuTj102rpmwZjs34Ny45twwezYrhn9NG_7eyg0WdKHvEbI9dg4fvtE">
  <br>
  Everlasting Summer / <a href="https://i.imgur.com/ZxUOFHp.gifv">view animated version</a><br>
</p>
<p align="center">
  <img width=300 src="https://s226myt.storage.yandex.net/rdisk/60365a6933b263554e4cb5429e8ac8243719e85b694b602bc8b6b82d22dfd3b0/5e937a27/bdoooSi8U1bZWHDWmel2x88CZTQCqU0PLvyS2B77821Y9GSDeQF_bNTlPT61lN1cCkCD29UF42-rHxXHJtx_Tw==?uid=293684676&filename=9input.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&etag=d9919d03bb154ab82d10407d6ec4cb15&hid=8b633477a6b6d0792e3027bd1f65f257&fsize=384642&media_type=image&rtoken=7LFbNndzE6fP&force_default=yes&ycrid=na-001df49d1f78506ea8f9aa03a9e0d228-downloader2f&ts=5a31dd2965580&s=2d11d75dd4f8a1ae0838a8a9ce1a40e8d83780c56a7ffe7ff6c9931c86367b35&pb=U2FsdGVkX183Dp8U1hAWYG12N6wHCEim5YX3lmZyZXGE_0AT7Mr12yCin3WQtz2sw8P-hyWvfhfVsvTnqOvlZxvVvJWnP3RLLskhHCWmKhc">
  <img width=300 src="https://s140man.storage.yandex.net/rdisk/d04763e32415bfb1bd78e05ac8d4f6190d50fdef2ed13df83e018b7ace5e8768/5e937a31/bdoooSi8U1bZWHDWmel2x9gTjEY6hm2Z1IqnUyN0bjrEbRdTXx5sLL9trtyMLdZ8j95tQVLNBJD_cjBEfRT3Xw==?uid=293684676&filename=9output.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&hid=38abc281755470b1c3d07f5c98dabc55&media_type=image&fsize=314090&etag=bd4b48ae986ed9cff52724be9a0d93bf&rtoken=oE7q1IyGqOgG&force_default=yes&ycrid=na-a04d694338a33269172f330ed03d1153-downloader2f&ts=5a31dd33e2e40&s=d252dfc1310ede39b03de196f0b25802c9121dfb6c6528ee2557b3f879a524f9&pb=U2FsdGVkX19ReuDbUy_XgB9noi811jnMct4zE8_UBrMXzfz_bVshvBg_ZvDDBS3LWfwJg6AtBRD1TkHbbOQ8Q6FJZzmNVm45fsqPFa3foHY">
  <br>
  VA-11 Hall-A: Cyberpunk Bartender Action / <a href="https://i.imgur.com/7osrDHE.gifv">view animated version</a><br>
</p>
<p align="center">
  <img width=300 src="https://s79myt.storage.yandex.net/rdisk/1a4eeda904df89cbfac9ea2b2966743a2d2f8cff7a155c6b3f21ccdb9e961617/5e937e63/bdoooSi8U1bZWHDWmel2xyFN-tiqDNF8KnKSvenHrL3qsr8aP-akPVYIJBGt8uKxuuUG-bifdza5r3Kk4VlLGQ==?uid=293684676&filename=13input.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&hid=256f6d0d38dfca1d24ad5016e0db5655&fsize=751150&etag=ee3981e6b121a494559eb51d781d72e1&media_type=image&rtoken=pSeJtzHkQYIa&force_default=yes&ycrid=na-70c92252c39f834f66375c7cfa888c57-downloader12f&ts=5a31e13421ec0&s=941ffa35b5715165c0ca043f7f7499aa8b93cb33e3169c11f141ed29a7ba72b7&pb=U2FsdGVkX19x3u4ZORmy6W1biHpF4Uj2ToMwx-WUr6E5OhmdzLzruSpEjXfgqHjQPLXHQMF5crEbEjbOtNZpujSUaV9R73jORy60QteJCS0">
  <img width=300 src="https://s559sas.storage.yandex.net/rdisk/262caec81d48acddb9f8c7d74ebb6289de4fea1deefd5bca14603263b3e40280/5e937e75/bdoooSi8U1bZWHDWmel2xzx9Bn2IRA0zme6rzVtW0RLMPC8IPKCksRyDA6HpZEDyUfTnhXWBGVhNLmJqBnnyjg==?uid=293684676&filename=13output.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&owner_uid=293684676&fsize=397323&media_type=image&hid=579c50e7dfd87d141883584234690dbf&etag=ea1e0c79085549a75b6414d5eac8188a&rtoken=jxtWPIEHmF7X&force_default=yes&ycrid=na-d8357de337e0e3011ec00bd67110d712-downloader7e&ts=5a31e1454c740&s=f387e5bd96892d2f3e48b2cf11348504738b30242aaaf8b33613b19fad31defd&pb=U2FsdGVkX1_MfMTh8optt8wTdpk5Zrl68ZJyVqNwWhv6PDGB2rjZzsk9s9rw7-LdHlHDx4YIT4zlJ7dRLL5EV49tfuV8S21830mSp9VMN-w">
  <br>
  <a href="https://i.imgur.com/sZCYU9B.gifv">view animated version</a><br>
</p>