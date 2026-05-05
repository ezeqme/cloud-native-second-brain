---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Keynote Sessions"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Ralph Squillace", "Principal Product Manager", "Microsoft", "Michelle Dhanani", "Principal Software Engineer", "Fermyon Technologies", "Kai Walter", "Distinguished Architect", "Z..."]
sched_url: https://kccnceu2024.sched.com/event/1YhJM/keynote-panel-discussion-revolutionizing-cloud-native-architectures-with-webassembly-ralph-squillace-principal-product-manager-microsoft-michelle-dhanani-principal-software-engineer-fermyon-technologies-kai-walter-distinguished-architect-zeiss
youtube_search_url: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Revolutionizing+Cloud+Native+Architectures+with+WebAssembly+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keynote Panel Discussion: Revolutionizing Cloud Native Architectures with WebAssembly - Ralph Squillace, Principal Product Manager, Microsoft; Michelle Dhanani, Principal Software Engineer, Fermyon Technologies; Kai Walter, Distinguished Architect, Z...

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: France / Paris
- Speakers: Ralph Squillace, Principal Product Manager, Microsoft, Michelle Dhanani, Principal Software Engineer, Fermyon Technologies, Kai Walter, Distinguished Architect, Z...
- Schedule: https://kccnceu2024.sched.com/event/1YhJM/keynote-panel-discussion-revolutionizing-cloud-native-architectures-with-webassembly-ralph-squillace-principal-product-manager-microsoft-michelle-dhanani-principal-software-engineer-fermyon-technologies-kai-walter-distinguished-architect-zeiss
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Revolutionizing+Cloud+Native+Architectures+with+WebAssembly+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keynote Panel Discussion: Revolutionizing Cloud Native Architectures with WebAssembly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhJM/keynote-panel-discussion-revolutionizing-cloud-native-architectures-with-webassembly-ralph-squillace-principal-product-manager-microsoft-michelle-dhanani-principal-software-engineer-fermyon-technologies-kai-walter-distinguished-architect-zeiss
- YouTube search: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Revolutionizing+Cloud+Native+Architectures+with+WebAssembly+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tu8a-GefJL8
- YouTube title: Keynote Panel Discussion: Revolutionizing Cloud Native Architectures with WebAssembly
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keynote-panel-discussion-revolutionizing-cloud-native-architectures-wi/tu8a-GefJL8.txt
- Transcript chars: 11998
- Keywords: assembly, container, workloads, allows, resources, already, basically, actually, runtime, containers, operator, cluster, projects, orders, weight, heavyweight, operating, running

### Resumo baseado na transcript

so I've recently gotten into boxing I don't actually box I mostly just Swatch from the comfort of my couch and in boxing there are weight classes like heavyweight middle weight lightweight and so on and it's exactly how it sounds a boxer must meet a certain weight to box within a class and these weight classes is remind me of the clouds of the waves of cloud computing so first up you've got your virtual machines this is your heavyweight class being in the heavyweight class in boxing means

### Excerpt da transcript

so I've recently gotten into boxing I don't actually box I mostly just Swatch from the comfort of my couch and in boxing there are weight classes like heavyweight middle weight lightweight and so on and it's exactly how it sounds a boxer must meet a certain weight to box within a class and these weight classes is remind me of the clouds of the waves of cloud computing so first up you've got your virtual machines this is your heavyweight class being in the heavyweight class in boxing means you are powerful but if you get knocked down it's G to take some time for you to get back up that's basic physics right virtual machines are the OG heavyweight runtime for the cloud often they take minutes to start but they contain an entire operating system from kernel to Applications so you can do a lot with them a container is lighter and smaller and in the world of cloud computing this would be your middleweight class middleweight strikes a balance between speed and power containers have given us the perfect environment for running a single long running server they take seconds not minutes to start and consume fewer resources than virtual machines now add to that web assembly the third wave of cloud computing this is your lightweight class Speed and Agility is the name of the game here compile your app once directly to the web assembly binary format and use that same binary across multiple architectures and operating systems with no changes and a web assembly app can be cold started in about half a millisecond half a millisecond making it vastly faster than even making its startup speed vastly faster than even containers so how do we run web assembly on kubernetes and incloud Native environments I'm going to talk to you about spin Cube today which is a project that helps you do just that so this is a spin app custom resource in kubernetes online six is a reference to an oci artifact containing a web assembly binary yeah that's a thing you can do so behind this uh spin app custom resource lives a spin operator once I uh apply my spin apps to my cluster we're going to see it running uh in our cluster here the spin app the spin operator will actually pick it up and deploy the coresponding deployment pod and service and it's configuring the Pod to use a wasm runtime instead of a container runtime to execute our app so on the outside you still have your pods and services same as usual but on the inside they're actually web assembly apps not containers this is that same app
