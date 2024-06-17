cat << 'EOF' > "${TARGET_DIR}/root/.bashrc"
# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
NC='\033[0m' # No Color

# Prompt with colors
PS1="\[$GREEN\]\u@\h\[$WHITE\]:\[$BLUE\]\w\[$NC\]\$ "

# Alias definitions
alias ls='ls --color=auto'

# Colorize directory listings
LS_COLORS='di=1;36:fi=0:ln=35:pi=5:so=5:bd=5:cd=5:or=31:mi=0:ex=32:*.cmd=32:*.exe=32:*.com=32:*.bat=32:*.btm=32:*.dll=32:*.tar=32:*.tbz=32:*.tgz=32:*.rpm=32:*.deb=32:*.arj=32:*.taz=32:*.lzh=32:*.zip=32:*.zoo=32:*.z=32:*.Z=32:*.gz=32:*.bz2=32:*.tb2=32:*.tz2=32:*.tbz2=32:*.xz=32:*.avi=32:*.bmp=32:*.fli=32:*.gif=32:*.jpg=32:*.jpeg=32:*.mng=32:*.mov=32:*.mpg=32:*.pcx=32:*.pbm=32:*.pgm=32:*.png=32:*.ppm=32:*.tga=32:*.tif=32:*.xbm=32:*.xpm=32:*.dl=32:*.gl=32:*.wmv=32:*.aiff=32:*.au=32:*.mid=32:*.mp3=32:*.ogg=32:*.voc=32:*.wav=32:'

export LS_COLORS

# Add your own aliases and functions below
EOF

# Source the modified .bashrc file to apply changes immediately
source "${TARGET_DIR}/root/.bashrc"