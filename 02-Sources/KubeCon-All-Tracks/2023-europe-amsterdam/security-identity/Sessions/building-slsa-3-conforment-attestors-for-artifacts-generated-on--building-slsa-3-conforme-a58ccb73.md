---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Ian Lewis", "Asra Ali", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HydG/building-slsa-3-conforment-attestors-for-artifacts-generated-on-github-ian-lewis-asra-ali-google
youtube_search_url: https://www.youtube.com/results?search_query=Building+SLSA+3+Conforment+Attestors+for+Artifacts+Generated+on+GitHub+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Building SLSA 3 Conforment Attestors for Artifacts Generated on GitHub - Ian Lewis & Asra Ali, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ian Lewis, Asra Ali, Google
- Schedule: https://kccnceu2023.sched.com/event/1HydG/building-slsa-3-conforment-attestors-for-artifacts-generated-on-github-ian-lewis-asra-ali-google
- Busca YouTube: https://www.youtube.com/results?search_query=Building+SLSA+3+Conforment+Attestors+for+Artifacts+Generated+on+GitHub+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Building SLSA 3 Conforment Attestors for Artifacts Generated on GitHub.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HydG/building-slsa-3-conforment-attestors-for-artifacts-generated-on-github-ian-lewis-asra-ali-google
- YouTube search: https://www.youtube.com/results?search_query=Building+SLSA+3+Conforment+Attestors+for+Artifacts+Generated+on+GitHub+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Aq3ND6xmkyU
- YouTube title: Building SLSA 3 Conforment Attestors for Artifacts Generated on GitHub- Ian Lewis & Asra Ali, Google
- Match score: 0.923
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/building-slsa-3-conforment-attestors-for-artifacts-generated-on-github/Aq3ND6xmkyU.txt
- Transcript chars: 27699
- Keywords: tester, actually, attestation, source, process, package, software, create, github, provenance, platform, itself, container, testers, framework, already, ecosystems, pipeline

### Resumo baseado na transcript

hello everyone Welcome to our talk on building salsa 3 Conformity testers for artifacts generated on GitHub my name is Esther Ellie and I'm a software engineer on the Google open source security team and I also work on Faison a team about open source FHA transpilers this is my co-speaker Ian Lewis uh yes I'm Ian Lewis I'm a developer Advocate at Google Cloud um working on container and supply chain security and uh I'm currently on loan to the Google open source security team uh working on salsa

### Excerpt da transcript

hello everyone Welcome to our talk on building salsa 3 Conformity testers for artifacts generated on GitHub my name is Esther Ellie and I'm a software engineer on the Google open source security team and I also work on Faison a team about open source FHA transpilers this is my co-speaker Ian Lewis uh yes I'm Ian Lewis I'm a developer Advocate at Google Cloud um working on container and supply chain security and uh I'm currently on loan to the Google open source security team uh working on salsa tooling all right thanks so first we'll be going over some background information on a testers and salsa 3 conformants then I'll be handing it over to Ian who will be discussing the challenges in building in a tester after that I'll go over an example a tester that we've created that's based on containers and then Ian will finally finish it off with diving into our templatized framework for our testers which we're calling the delegated a tester all right so many of you are already familiar with the software delivery Pipeline and the complexity that exists at each of these stages as an open source engineer one could be both a developer of a software delivery Pipeline and also a consumer of other people's software delivery pipelines even at the same time perhaps either by pulling in dependencies and so forth each software project has these dependencies that are pulled in from other Upstream developers and then used to create your own new software but during any of these stages from either the source and the build pulling independency and then all the way to deploying your resource anything can go wrong which may cause a software supply chain attack so the threats and attack factors in this are all kind of marked at each of these stages by through these links between let's say the source and the build and also what can occur at one of these stages like during the build and there have been many sort of countless examples of real attacks that have happened in the past couple of years in each one of these places so at the start for example you might imagine that code could be committed to a source repository repository or even perhaps that those Source Control Systems could be compromised themselves the same thing could happen maybe at the bills where maybe perhaps bad uh dependencies could be injected but also the build platform itself may be compromised and then likewise through all of these um a compromise could exist both at the place where uh translations are happeni
