---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Unclassified"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Dan Čermák", "SUSE"]
sched_url: https://kccnceu2022.sched.com/event/ytwd/lightning-talk-what-made-your-container-fat-visualizing-the-size-of-container-layers-dan-cermak-suse
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+What+Made+Your+Container+Fat%3F+Visualizing+the+Size+of+Container+Layers+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: What Made Your Container Fat? Visualizing the Size of Container Layers - Dan Čermák, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: Spain / Valencia
- Speakers: Dan Čermák, SUSE
- Schedule: https://kccnceu2022.sched.com/event/ytwd/lightning-talk-what-made-your-container-fat-visualizing-the-size-of-container-layers-dan-cermak-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+What+Made+Your+Container+Fat%3F+Visualizing+the+Size+of+Container+Layers+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: What Made Your Container Fat? Visualizing the Size of Container Layers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwd/lightning-talk-what-made-your-container-fat-visualizing-the-size-of-container-layers-dan-cermak-suse
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+What+Made+Your+Container+Fat%3F+Visualizing+the+Size+of+Container+Layers+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WpGmbJWr19E
- YouTube title: Lightning Talk: What Made Your Container Fat? Visualizing the Size of Container Layers - Dan Čermák
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-what-made-your-container-fat-visualizing-the-size-of-co/WpGmbJWr19E.txt
- Transcript chars: 4608
- Keywords: container, layers, actual, images, pretty, developer, interesting, sunburst, essentially, various, lightning, thanks, occasionally, containers, bigger, analyzing, actually, select

### Resumo baseado na transcript

hi thanks everyone so thanks for making it in such a numerous numbers to my lightning talk what made your container fat so few words first about me i'm a software developer working at susa part of the developer engagement program i also do other stuff mostly in developer tools testing i'm also a member of the fedora community and in case you are not totally bored after this talk you can also stalk me on some social media where i occasionally write maybe interesting stuff you can be the

### Excerpt da transcript

hi thanks everyone so thanks for making it in such a numerous numbers to my lightning talk what made your container fat so few words first about me i'm a software developer working at susa part of the developer engagement program i also do other stuff mostly in developer tools testing i'm also a member of the fedora community and in case you are not totally bored after this talk you can also stalk me on some social media where i occasionally write maybe interesting stuff you can be the judge of that but let's get to the actual topic at hand so we at souza we do all kinds of stuff and one of them is building containers and if you start building containers you occasionally run into the issue well gosh the image got bigger oh well where and then you start unpacking container images and you start analyzing them and it starts to get confusing pretty pretty easily pretty fast so where's actually the size increase coming from so maybe you want to take a closer look then you figure out okay i have a big container image and got 20 layers which layer is now the actual culprit where where the where did it get the big and there you can't really go into the old trick that you just launched the container image you install ncdu and you take a look because then you have to find the actual the actual layer so you can unpack it and you put it somewhere in your temper temperfest and you get super and after you've done it 50 times you have a huge temporary directory with all kinds of layers extracted and you forgot which one is the actual one that you are looking for so um then so that's unfortunately a pretty cool tool for that it's called dive but maybe you like prettier graphs and i like the gnome disk usage analyzer which produces pretty nice sunburst charts and i wanted something like that for container images as well and also what would be really nice being able to compare images side by side and since i didn't see something for that i wrote something so let me let me show you this tool that essentially shows you a sunburst graph of a container layer so if you want to see what actually is big in your container image on the file system you can do it with that so let's jump into a short demo what the how the tool looks like this is a real it's just a web app so you can open it in your web browser you give it a container image it will show you the various platforms by which you can pull it so you can select any architecture that you'd like you tell it to anna to pull it do
