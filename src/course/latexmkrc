# set compiler - xelatex
$pdf_mode = 1;
$pdflatex = 'xelatex %O %S';

# build dir
$out_dir = 'build';

# simply output
$silent = 1;

# continuous view
$preview_continuous_mode = 1;

# automatic cleaning of temporary files
$clean_ext = 'aux bbl blg log out toc lof lot fls fdb_latexmk';


# use biber
$bibtex_use = 2;
add_cus_dep('bib', 'bbl', 0, 'run_biber');
sub run_biber {
    system("biber '$_[0]'");
}

