---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Andrew Block", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFyi/project-lightning-talk-modelpack-standardizing-the-packaging-and-distribution-of-aiml-models-andrew-block-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Modelpack%3A+Standardizing+The+Packaging+And+Distribution+Of+AI%2FMl+Models+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Modelpack: Standardizing The Packaging And Distribution Of AI/Ml Models - Andrew Block, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Andrew Block, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFyi/project-lightning-talk-modelpack-standardizing-the-packaging-and-distribution-of-aiml-models-andrew-block-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Modelpack%3A+Standardizing+The+Packaging+And+Distribution+Of+AI%2FMl+Models+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Modelpack: Standardizing The Packaging And Distribution Of AI/Ml Models.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFyi/project-lightning-talk-modelpack-standardizing-the-packaging-and-distribution-of-aiml-models-andrew-block-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Modelpack%3A+Standardizing+The+Packaging+And+Distribution+Of+AI%2FMl+Models+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gR-3Sdh1AKU
- YouTube title: Project Lightning Talk: Modelpack: Standardizing The Packaging And Distribution Of... Andrew Block
- Match score: 0.994
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-modelpack-standardizing-the-packaging-and-distr/gR-3Sdh1AKU.txt
- Transcript chars: 5308
- Keywords: content, models, container, manage, artifacts, distribution, tooling, benefits, native, already, package, potentially, finally, standards, leverage, images, existing, capabilities

### Resumo baseado na transcript

I'm going to talk to you today about Model Pack and its ability to distribute and package AI and ML models. Now, for those of you who work in the AI and ML space, it's a challenging time. And if you're using Kubernetes, there's a entire management ecosystem that you have to potentially deal with. And you get all the benefits of version management, distribution, access control, and security and compliance out of the box. Use Model Pack use the model CTL to pull down it locally to your machine, or you can use a container runtime using Docker, Podman, or in Kubernetes, you can then leverage the CSI driver or the the out-of-the-box image volume source. So, if you want to go ahead and learn more about Model Pack, while you're here, you're number one, so that's one way to learn.

### Excerpt da transcript

All right, everyone. I'm going to talk to you today about Model Pack and its ability to distribute and package AI and ML models. Now, for those of you who work in the AI and ML space, it's a challenging time. It's a challenging time because you have to manage a lot of the content. And there are three ways that you have to potentially manage this content. One is you have to package your content. And when you package any content, you're going to have various files, folders, archives, different types of data. You then have proprietary information that might be in those models. You also need to figure out how to store the models. You're storing them in a variety of locations. Is it going to be an S3 bucket? Is it going to be within Git? Is it going to be in some proprietary model store that your provider or whatever tooling you're using? And finally, how are you serving the content? You know, each framework is going to have its own type of of content ability. You might have like if you're using Python, it may have its own idiosyncrasies on top of that.

And if you're using Kubernetes, there's a entire management ecosystem that you have to potentially deal with. Those are all challenges. So, that's why the community came up with a project called Model Pack. Model Pack is a vendor neutral open standards way for managing AI and ML models. It is a sandbox project in the CNCF since last year in May 2025. So, how do you go ahead and leverage the power of Model Pack? Well, first of all, it packages AI and ML models as OCI artifacts using standardized and easy distribution and that can be used for easy distribution and consumption. Uh its benefits. The benefits of Model Pack are easy. First of all, you can apply your open cloud native standards. So, we're all here. We're all part of the cloud native community. We're just reusing a lot of the abilities that are already out there in the community using the open container initiative. Now, OCI, it is, you may or may not know, is a standard for how you manage container images. Well, recently, you can now go ahead and manage other things aside from container images using a concept called the OCI artifacts.

So, you know, Robert mentioned earlier, one way you can also manage use artifacts is through Helm. Helm charts can now be distributed as OCI artifacts. Some of the benefits in addition to not only using cloud native standards is that you can use reuse your existing infrastructure because you can use basically everything
