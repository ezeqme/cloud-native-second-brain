---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Anais Urlichs", "Aqua Security", "Shengwen Yu", "VMware"]
sched_url: https://kccnceu2024.sched.com/event/1YeRK/leveraging-oci-11-for-enhanced-sbom-integration-and-vulnerability-scanning-in-harbor-anais-urlichs-aqua-security-shengwen-yu-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Leveraging+OCI+1.1+for+Enhanced+SBOM+Integration+and+Vulnerability+Scanning+in+Harbor+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Leveraging OCI 1.1 for Enhanced SBOM Integration and Vulnerability Scanning in Harbor - Anais Urlichs, Aqua Security & Shengwen Yu, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: France / Paris
- Speakers: Anais Urlichs, Aqua Security, Shengwen Yu, VMware
- Schedule: https://kccnceu2024.sched.com/event/1YeRK/leveraging-oci-11-for-enhanced-sbom-integration-and-vulnerability-scanning-in-harbor-anais-urlichs-aqua-security-shengwen-yu-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Leveraging+OCI+1.1+for+Enhanced+SBOM+Integration+and+Vulnerability+Scanning+in+Harbor+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Leveraging OCI 1.1 for Enhanced SBOM Integration and Vulnerability Scanning in Harbor.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRK/leveraging-oci-11-for-enhanced-sbom-integration-and-vulnerability-scanning-in-harbor-anais-urlichs-aqua-security-shengwen-yu-vmware
- YouTube search: https://www.youtube.com/results?search_query=Leveraging+OCI+1.1+for+Enhanced+SBOM+Integration+and+Vulnerability+Scanning+in+Harbor+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ABbds5-zSqk
- YouTube title: Leveraging OCI 1.1 for Enhanced SBOM Integration and Vulnerability Scanning in Harbor
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/leveraging-oci-1-1-for-enhanced-sbom-integration-and-vulnerability-sca/ABbds5-zSqk.txt
- Transcript chars: 23567
- Keywords: harbor, container, scanner, artifact, images, registry, generate, trivia, accessory, basically, subject, scanning, version, vulnerability, automatically, actually, resources, manually

### Resumo baseado na transcript

thank you everybody for coming to our talk on a Friday afternoon last day of cucon for leveraging oci 1.1 for enhanced espam integration and vulnerability scanning in Harbor I'm here with my co-speaker shangu my name is an or I'm jumping in fore who can sadly not be here today due to family commitments hi everyone love to see you all in this group confession my name is sh a software engineer from br I've been in the cloud computing industry for about 3 years now and currently I incidents uh security issues we talk about how we can make our services more observable we don't necessarily talk about what can we do to prepare for security incidents now one of the things that organizations can do is generate s bombs s bombs allow you to easily identify what resources you use so in a case there are new vulnerabilities released you can easily identify if you affected by those vulnerabilities the overall average uh cost per incident per year increases each year and organizations have to find new accessory we have one plan feature which is scanning as spom for one abilities this feature is uh this feature plan this picture will be configur will be designed to be configurable VI the system settings and it is it it is it SC Thea the ux and just your use cases as well and if you have any questions once you try it out yourself uh also reach out in the cncf slack channel in Harbor and we...

### Excerpt da transcript

thank you everybody for coming to our talk on a Friday afternoon last day of cucon for leveraging oci 1.1 for enhanced espam integration and vulnerability scanning in Harbor I'm here with my co-speaker shangu my name is an or I'm jumping in fore who can sadly not be here today due to family commitments hi everyone love to see you all in this group confession my name is sh a software engineer from br I've been in the cloud computing industry for about 3 years now and currently I am a main of the har project and my daily work includes release management of the har project and Har osss and uh issue charge and PR review in the of both them and J pel maintenance also Bo fixing and I'm really honored and th to be here and can't wait to share with you the topic of Leverage o spe 1. one for enhanced is is for integration and scanning awesome so this talk was originally submitted as well by tap fakuda who's working with me on the open source team in aqua security now he's the person who created trivy originally which will be used as well doing this talk now I'm at open source developer Advocate at Aqua security and closely working with tapa and on trivy now for the agenda for those who are also watching the recording in uh this is what we be covered in this talk first a little bit of an introduction and background on what are es bombs why do we even need es bombs then we will look at the oci spec version 1.1 as well as their referral API we will look at the esam integration in Harbor and the harbor PL plugable scanner spec version 1.2 as well as how we integrate it in Harbor scanner trivia integration we will have a live demo and hopefully lots of time for Q&A all right and I'm just curious like how many of you have heard of Harbor please raise your hand cool nice and uh how many of you have regularly occasionally used har um e perect registry for your company or for yourself to show images cool like for those of you who are not familiar with it h is a CF graduate project with more than 22,000 starts and uh around 25,000 Forks in GitHub and uh how is also an open source registry and that allows users to with ro based access to p and push images and uh our mission is to be the cloud crafted is to be the crafted Cloud native repository forat awesome who has heard of trivy before who uses trivia with out Harbor who uses trivia in Harbor awesome so maybe after this talk more people are going to use trivia within Harbor so trivia is an all-in-one clout native opsource s
