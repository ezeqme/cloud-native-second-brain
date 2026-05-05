---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Tao Peng", "Maintainer"]
sched_url: https://kccncna2025.sched.com/event/27d5g/project-lightning-talk-modelpack-an-open-standard-for-packaging-distributing-and-running-llms-in-cloud-native-ecosystems-tao-peng-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ModelPack%3A+An+Open+Standard+for+Packaging%2C+Distributing%2C+and+Running+LLMs+In+Cloud-Native+Ecosystems+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: ModelPack: An Open Standard for Packaging, Distributing, and Running LLMs In Cloud-Native Ecosystems - Tao Peng, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Tao Peng, Maintainer
- Schedule: https://kccncna2025.sched.com/event/27d5g/project-lightning-talk-modelpack-an-open-standard-for-packaging-distributing-and-running-llms-in-cloud-native-ecosystems-tao-peng-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ModelPack%3A+An+Open+Standard+for+Packaging%2C+Distributing%2C+and+Running+LLMs+In+Cloud-Native+Ecosystems+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: ModelPack: An Open Standard for Packaging, Distributing, and Running LLMs In Cloud-Native Ecosystems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d5g/project-lightning-talk-modelpack-an-open-standard-for-packaging-distributing-and-running-llms-in-cloud-native-ecosystems-tao-peng-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ModelPack%3A+An+Open+Standard+for+Packaging%2C+Distributing%2C+and+Running+LLMs+In+Cloud-Native+Ecosystems+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kb9L9E5matI
- YouTube title: Project Lightning Talk: ModelPack: An Open Standard for Packaging, Distributing, and... Tao Peng
- Match score: 0.874
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-modelpack-an-open-standard-for-packaging-distri/kb9L9E5matI.txt
- Transcript chars: 2604
- Keywords: packaging, specification, models, basically, harbor, integration, distributing, running, ecosystem, pretty, container, images, weights, format, supposed, package, distribute, artifact

### Resumo baseado na transcript

Hi guys, I'm Top from Mr and I'm going to talk about model bank which is a open stand for packaging distributing and running in cloud native ecosystem. So um we are a pretty new project established this year and donating to Sensf on May and uh our target is I believe most of you are familiar with container images and we are actually packaging your AM code and weights into a similar Then we introduce how they integrate model pack in their in harbor and make sure your your model can be stored in hover properly and also we have another presentation on Django flight that is basically a P2P networks or storage network and then that

### Excerpt da transcript

Hi guys, I'm Top from Mr and I'm going to talk about model bank which is a open stand for packaging distributing and running in cloud native ecosystem. So um we are a pretty new project established this year and donating to Sensf on May and uh our target is I believe most of you are familiar with container images and we are actually packaging your AM code and weights into a similar format like container image and this is this is supposed to be a vendor neutral and open source specification to do this and help you to package, distribute and run models in a cloudative environment. So how does it work? First, we provide a variety of tools that helps you to build and push your your air models into and then OCI artifact following the model format specification. So basically if you have a a git repository hosting all your weights and configurations and you can use our tools to make to package them into a model artifact which is basically like a content image image that has a manifest describing all the contents in the image and also you can push it into any OCI compatible registries such as Docker, Docker Hub, Harbor or any cloud registries and when you have it stored on the with within the registry you can use and different tools to pull down the the model model images and use it with kumis and mount it as a local volume and then you can just access it from your from your port it's like accessing in local storage.

So we've been working with the ecosystem and make sure this works and we have kubernetes integration have hover integration cryo integration and jango flag for distribution. So this is this is pretty much working in progress and so where where you can find us we have we we will show showcase this in the chaos tomorrow afternoon and there will be two united presentations on this. The first one is pro project update from harbor maintainers. Then we introduce how they integrate model pack in their in harbor and make sure your your model can be stored in hover properly and also we have another presentation on Django flight that is basically a P2P networks or storage network and then that is supposed to distribute the AI AI models efficiently in your cluster. And also how to get in touch we have we just have our website up to date and we you can find us on snack and also on GitHub and we have if you are interested in the in the model spec details you can just check out the specification markdown and also we have a simple getting started document to help y
