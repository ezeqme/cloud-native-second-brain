---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Runtimes"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Kohei Tokunaga", "NTT Corporation", "Tao Peng", "Ant Financial"]
sched_url: https://kccncna2021.sched.com/event/lV2a/faster-container-image-distribution-on-a-variety-of-tools-with-lazy-pulling-kohei-tokunaga-ntt-corporation-tao-peng-ant-financial
youtube_search_url: https://www.youtube.com/results?search_query=Faster+Container+Image+Distribution+on+a+Variety+of+Tools+with+Lazy+Pulling+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Faster Container Image Distribution on a Variety of Tools with Lazy Pulling - Kohei Tokunaga, NTT Corporation & Tao Peng, Ant Financial

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Runtimes]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United States / Los Angeles
- Speakers: Kohei Tokunaga, NTT Corporation, Tao Peng, Ant Financial
- Schedule: https://kccncna2021.sched.com/event/lV2a/faster-container-image-distribution-on-a-variety-of-tools-with-lazy-pulling-kohei-tokunaga-ntt-corporation-tao-peng-ant-financial
- Busca YouTube: https://www.youtube.com/results?search_query=Faster+Container+Image+Distribution+on+a+Variety+of+Tools+with+Lazy+Pulling+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Faster Container Image Distribution on a Variety of Tools with Lazy Pulling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2a/faster-container-image-distribution-on-a-variety-of-tools-with-lazy-pulling-kohei-tokunaga-ntt-corporation-tao-peng-ant-financial
- YouTube search: https://www.youtube.com/results?search_query=Faster+Container+Image+Distribution+on+a+Variety+of+Tools+with+Lazy+Pulling+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=K2VlZE7lDjI
- YouTube title: Faster Container Image Distribution on a Variety of Tools with Lazy... - Kohei Tokunaga & Tao Peng
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/faster-container-image-distribution-on-a-variety-of-tools-with-lazy-pu/K2VlZE7lDjI.txt
- Transcript chars: 19858
- Keywords: container, images, support, playing, format, another, registry, compatible, supports, enables, conversion, docker, remote, called, snapshot, started, seconds, convert

### Resumo baseado na transcript

hi i'm kohei tuk-naga from ntt corporation i'm a reviewer of contenary and a maintenance of build kit i'm joined today by tao peng and group today we will introduce and deep dive into faster container image distribution technique discussed in the community which is called lazy blink first i'm gonna give you a brief introduction to lazy blink playing continent image is known as one of the time consuming steps in the container lifecycle this has been affected various kinds of use cases including batch job execution and building

### Excerpt da transcript

hi i'm kohei tuk-naga from ntt corporation i'm a reviewer of contenary and a maintenance of build kit i'm joined today by tao peng and group today we will introduce and deep dive into faster container image distribution technique discussed in the community which is called lazy blink first i'm gonna give you a brief introduction to lazy blink playing continent image is known as one of the time consuming steps in the container lifecycle this has been affected various kinds of use cases including batch job execution and building images their efforts to minimize the size of container images but not all images are minimizable research shows that playing packages accounts for 76 percent of container start time but only 6.4 percent of that data is read the root cause of this issue is the current ocl images in these images each root fs layer is formatted as star and optionally plus compression tar is not seekable and cannot perform parallel extraction so when we start the container we first need to download the entire image content to the node then extract each layer sequentially if the image is large starting up the container will take long for solving this issue several osseo alternative image formats are discussed in the community they aim to speed up container cold start so they are sometimes called as accelerated images accelerated images enables a sort of technique of container image distribution called lazy blink this allows container runtimes to start up continuous before the entire image contents being locally available instead necessary chunks of content like files are downloaded from the registry on demand in this talk we put focus on two of image formats and deep dive into how lazy playing is achieved instagram is also a compatible image format for lazy blink this comes with prefetch optimization and content verification this is proposed as a backward compatible extension to ocr image specification nidus is a lazy buildable image format with perfect chunk deduplication and e2e dental integrity this is compatible with osi distribution spec and oci artifact spec this is incompatible to all set image specification so this is proposed as ocr image spec v2 format first let's take a look deeper look at each third digit image format easter egg is an image format for legibling this is backward compatible to the current ocr image specification so this is lazy poolable from oci compliant registries as shown in the following figure and even legacy and lazy playin
