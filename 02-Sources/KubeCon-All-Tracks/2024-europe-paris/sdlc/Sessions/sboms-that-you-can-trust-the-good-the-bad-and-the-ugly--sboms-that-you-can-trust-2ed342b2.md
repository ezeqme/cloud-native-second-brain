---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["AI ML", "Security"]
speakers: ["Miguel Martinez", "Daniel Liszka", "Chainloop"]
sched_url: https://kccnceu2024.sched.com/event/1YeSg/sboms-that-you-can-trust-the-good-the-bad-and-the-ugly-miguel-martinez-daniel-liszka-chainloop
youtube_search_url: https://www.youtube.com/results?search_query=SBOMs+That+You+Can+Trust+-+the+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SBOMs That You Can Trust - the Good, the Bad, and the Ugly - Miguel Martinez & Daniel Liszka, Chainloop

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: France / Paris
- Speakers: Miguel Martinez, Daniel Liszka, Chainloop
- Schedule: https://kccnceu2024.sched.com/event/1YeSg/sboms-that-you-can-trust-the-good-the-bad-and-the-ugly-miguel-martinez-daniel-liszka-chainloop
- Busca YouTube: https://www.youtube.com/results?search_query=SBOMs+That+You+Can+Trust+-+the+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SBOMs That You Can Trust - the Good, the Bad, and the Ugly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSg/sboms-that-you-can-trust-the-good-the-bad-and-the-ugly-miguel-martinez-daniel-liszka-chainloop
- YouTube search: https://www.youtube.com/results?search_query=SBOMs+That+You+Can+Trust+-+the+Good%2C+the+Bad%2C+and+the+Ugly+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H3uyoJHXVX8
- YouTube title: SBOMs That You Can Trust - the Good, the Bad, and the Ugly - Miguel Martinez & Daniel Liszka
- Match score: 0.863
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sboms-that-you-can-trust-the-good-the-bad-and-the-ugly/H3uyoJHXVX8.txt
- Transcript chars: 23236
- Keywords: metadata, security, storage, artifacts, attestation, registry, information, actually, compliance, github, integrity, source, materials, making, organization, software, course, material

### Resumo baseado na transcript

hi everybody um thank you for being here yeah it's 3M on Friday so we really appreciate the fact that you're here today um my name is Miguel this is Daniel we are the co-founders at chain loop chain loop is an open source project that allows you to collect secure and distribute sofware supply chain metadata but before that we used to work at bami and theare where we did a lot of cicd Automation and some of that automation is what behind today for example the the pami state is kept uh on the chain loop uh service so now let me go to developer so I have that project this is the Java uh demo spring pet clinic project I already showed you that we added that uh change that file to

### Excerpt da transcript

hi everybody um thank you for being here yeah it's 3M on Friday so we really appreciate the fact that you're here today um my name is Miguel this is Daniel we are the co-founders at chain loop chain loop is an open source project that allows you to collect secure and distribute sofware supply chain metadata but before that we used to work at bami and theare where we did a lot of cicd Automation and some of that automation is what behind today for example the the pami container images or Helm charts that you might be using today but today we are here to talk about something else today we're going to be talking about what does it mean U trustworthy so bu materials why you should care about it now then we're going to be looking at different solutions that can help us to get to reach that goal then we're going to have a demo and finally some closing thoughts about what could come next so we're going to start with this traditional cic pipeline all the way from source code to production so you might be building a a a go binary at build time then you're packaging it in a container image and then pushing it to O registry and finally deploying it to to a this cluster but the interesting bit and the reason we put this diagram here is because eventually and this might have happened to you already you will get other stakeholders in your organization that want to get they will have a saying on how you are releasing software so for example you might have a security team asking for a mechanism to manage vulnerabilities or you might have a compliance team that want to double check they want to make sure that some open source licenses for some third parties don't go through and of course you might have an Sr team or a platform team that wants to make sure that the system is healthy so on so forth and this gets more complex the the the pick the organization is and we're going to see that later but in our experience these uh many of these use cases start with sare supply chain metadata and by S supply chain metadata we mean any piece of information any context that you can get about what you're building and how you're doing it so this can go from CVS scans Vex files some legal security architecture reviews QA test and of course so Bill materials so s Bill materials is a canonical example and for for those who hasn't heard of it it's just a standardized machine readable list of packages licenses and so on so you might have been asked on this again this might sound very famili
