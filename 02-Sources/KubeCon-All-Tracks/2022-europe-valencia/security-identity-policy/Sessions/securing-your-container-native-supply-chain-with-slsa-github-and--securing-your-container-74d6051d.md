---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Security + Identity + Policy"
themes: ["AI ML", "Security", "Runtime Containers"]
speakers: ["Laurent Simon", "Google", "Priya Wadhwa", "Chainguard"]
sched_url: https://kccnceu2022.sched.com/event/ytq9/securing-your-container-native-supply-chain-with-slsa-github-and-tekton-laurent-simon-google-priya-wadhwa-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Your+Container+Native+Supply+Chain+with+SLSA%2C+Github+and+Tekton+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Securing Your Container Native Supply Chain with SLSA, Github and Tekton - Laurent Simon, Google & Priya Wadhwa, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[AI ML]], [[Security]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Laurent Simon, Google, Priya Wadhwa, Chainguard
- Schedule: https://kccnceu2022.sched.com/event/ytq9/securing-your-container-native-supply-chain-with-slsa-github-and-tekton-laurent-simon-google-priya-wadhwa-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Your+Container+Native+Supply+Chain+with+SLSA%2C+Github+and+Tekton+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Securing Your Container Native Supply Chain with SLSA, Github and Tekton.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytq9/securing-your-container-native-supply-chain-with-slsa-github-and-tekton-laurent-simon-google-priya-wadhwa-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Securing+Your+Container+Native+Supply+Chain+with+SLSA%2C+Github+and+Tekton+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iZpFtalj4xE
- YouTube title: Securing Your Container Native Supply Chain with SLSA, Github and Te... Laurent Simon & Priya Wadhwa
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/securing-your-container-native-supply-chain-with-slsa-github-and-tekto/iZpFtalj4xE.txt
- Transcript chars: 27277
- Keywords: github, provenance, certificate, container, supply, artifact, workflow, builder, tecton, actually, chains, signing, repository, cluster, trusted, software, source, registry

### Resumo baseado na transcript

hey everyone welcome to securing your container native supply chain with salsa at github and techton hi everyone i'm laurent i'm a security engineer at google i work on the open ssf scorecard project and supply chain security and i'm priya i'm a software engineer at chain guard i work on open source projects like six door and techton which we'll be talking about today and a bunch of other open source projects as well so you've probably heard a lot about software supply chain security in the news recently and sign the provenance and this is the resulting container image that we got so let's try to verify the problems okay so let's first verify that we can run our container image okay so this seems to be working we have our yellow hello world we can also run it by using the hash which is the same thing okay so at least our container image is working now let's verify the problems okay so salsa pronouns was verified and docker the docker container is printed that's that's what

### Excerpt da transcript

hey everyone welcome to securing your container native supply chain with salsa at github and techton hi everyone i'm laurent i'm a security engineer at google i work on the open ssf scorecard project and supply chain security and i'm priya i'm a software engineer at chain guard i work on open source projects like six door and techton which we'll be talking about today and a bunch of other open source projects as well so you've probably heard a lot about software supply chain security in the news recently as the graph shows attacks are on the rise and it's becoming really important to start to understand how you can secure your supply chain so let's take a recent attack as an example the npm caller package attack the attack happened just a few months ago and one of the maintainers decided to add an infinite loop in the package the code was never changed in the repository itself the maintainer pushed directly to the npm registry around 9 million projects depend on this package either directly or as a transitive dependency which is really scary as a developer it might be intimidating to know where to start when it comes to securing your supply chain so in this presentation we'll discuss practical steps you can take to start improving the security of your supply chain so the good news is that if you already use tacton or github workflows today there are a few easy steps that you can take to start securing your pipelines today so that's what we're going to be talking about in this talk let's jump right into it so a quick agenda for today when discussing supply chain security it's important to have some metrics or a framework to actually quantify how secure your supply chain is so that's why we're going to start by talking about salsa which is the framework we're going to be using to determine how secure our for our supply chains actually are then we'll jump into talking about six door which is a project we use for signing and verification and at the end of the talk we'll talk about how we bring salsa and sig stores together to achieve uh higher security levels in both tecton and github workflows with demos for each of those platforms so what is salsa salsa is an acronym that stands for supply chain levels for software artifacts you can think of salsa as a framework or a checklist basically a list of things that you want in your supply chain depending on how secure you want it to be salsa is not a tool or a service it's more a set of guiding principles some key
