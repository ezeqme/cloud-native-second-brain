---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["AI ML", "Security", "Runtime Containers", "SRE Reliability"]
speakers: ["Duane DeCapite", "VMware"]
sched_url: https://kccnceu2022.sched.com/event/ytwg/lightning-talk-scaling-container-builds-with-software-supply-chains-duane-decapite-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Scaling+Container+Builds+with+Software+Supply+Chains+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: Scaling Container Builds with Software Supply Chains - Duane DeCapite, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Duane DeCapite, VMware
- Schedule: https://kccnceu2022.sched.com/event/ytwg/lightning-talk-scaling-container-builds-with-software-supply-chains-duane-decapite-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Scaling+Container+Builds+with+Software+Supply+Chains+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: Scaling Container Builds with Software Supply Chains.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwg/lightning-talk-scaling-container-builds-with-software-supply-chains-duane-decapite-vmware
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Scaling+Container+Builds+with+Software+Supply+Chains+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BKegE2VQhnU
- YouTube title: Lightning Talk: Scaling Container Builds with Software Supply Chains - Duane DeCapite, VMware
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-scaling-container-builds-with-software-supply-chains/BKegE2VQhnU.txt
- Transcript chars: 4765
- Keywords: container, supply, cartographer, builds, designed, images, lightning, scaling, software, chains, flux, required, rebasing, rebuilt, package, happens, choreography, developer

### Resumo baseado na transcript

hello welcome to kubecon cloudnativecon i was fortunate to have been asked to give a lightning talk at the very first cloud native day and it's an honor to be with you here in valencia today in this lightning talk we will be discussing how to scale container bills with software supply chains with the build packs flux and cartographer projects so build packs is a cncf incubating project and is designed to simply go from source code to a running container there are no docker files required to build

### Excerpt da transcript

hello welcome to kubecon cloudnativecon i was fortunate to have been asked to give a lightning talk at the very first cloud native day and it's an honor to be with you here in valencia today in this lightning talk we will be discussing how to scale container bills with software supply chains with the build packs flux and cartographer projects so build packs is a cncf incubating project and is designed to simply go from source code to a running container there are no docker files required to build the container image so all that complexity just melts away it seems like also every day in the news we hear something about a software bill of materials or an s-bomb how it's either required or helpful build packs also creates an s bomb natively as part of the build process the build pack spec is involved with a logical mapping of layers to components so it makes it easy to do rebasing so this is really good for incremental builds which results in minimal data transfer when a full uh rebuilt is not required buildpack's api supports a wide variety of s-bom formats including sift spdx and cyclone dx the s-bom is created at build time which is nice because the user doesn't have to go back to scan the container to try to figure out what packages are in the container there's also a lot of really nice metadata in the s-bom also including what processes are available what run image was used to create the app image and as well as what build pack was used to create the app image the rebasing capability in build packs is key because large organizations could have hundreds of apps that use a common base os layer and if one package in that base os layer changes that means all the applications need to be rebuilt say all these applications use logging and say there's a base logging package say log4j that means every time the update happens in the base package the image needs to be rebuilt the build packs can make that easy because build pack images are built are composed of layers and the app images can all share a common runtime layer so in our example when that base os layer is updated and all the application images are affected build packs can upload a single patch copy of the os packages in the environment to the container registry so this rebase thing can happen very very quickly this can happen in the order of milliseconds and then a tool like kpac can automate the run of the build pack builds and then a supply chain like cartographer can then deploy the app images at sca
